#!/usr/bin/env bash
set -eux

if [[ "$OSTYPE" == "darwin"* ]]; then
    shopt -s expand_aliases
    chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
    alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
elif ! [[ $(google-chrome-stable --version) ]]; then
  echo "No 'google-chrome-stable' command found for running headless PDF generation" >&2
fi

if ! [[ $(python3 --version) ]]; then
  echo "No 'python' command found for running headless PDF generation" >&2
  exit 1
fi

OUTFILE=$(cat resume_data.yaml \
  | grep -E "^name:\s.+$" \
  | sed "s/name: //g" \
  | sed "s/ //g" \
  | xargs printf "%s-Resume.pdf\n")

rm -rf dist/
mkdir dist/

cp wasm-app/{*.js,*.html,*.css,*.ico} dist/
cp -r wasm-app/pkg/ dist/pkg/

rm -rf "$OUTFILE"

docker build -t cv-server:latest -f Dockerfile-server .
docker run --rm -d --name cv -p 8080:8080 cv-server

sleep 2

{
    google-chrome-stable --headless --disable-gpu \
        --run-all-compositor-stages-before-draw \
        --virtual-time-budget=20000 \
        --print-to-pdf="$OUTFILE" \
        http://127.0.0.1:8080

} || {
    printf ""
}

cp "$OUTFILE" dist/

docker logs cv
docker rm -f cv
