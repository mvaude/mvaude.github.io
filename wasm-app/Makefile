.PHONY: all build serve

all: build serve

build:
	wasm-pack build --target web
	rollup ./main.js --format iife --file ./pkg/bundle.js

serve:
	python3 -m http.server 8080
