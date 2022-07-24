#!/usr/bin/env bash
set -eux

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$DIR"

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

cd dist/
python3 -m http.server 8081 &
PID=$!
cd ..

sleep 1

{
    google-chrome-stable --headless --disable-gpu \
        --run-all-compositor-stages-before-draw \
        --virtual-time-budget=10000 \
        --print-to-pdf="$OUTFILE" \
        http://localhost:8081

} || {
    printf ""
}

kill "$PID"
rm -rf dist/
