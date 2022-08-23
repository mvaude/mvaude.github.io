.PHONY: help python rust build wasm all pdf python-ci ci
help:
	@echo "Resume as Code"
	@echo "========================"
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
		'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

python:  ## Build the Python protobuf interface
	cd protos && protoc resume.proto --python_out=../yaml-parser

rust:  ## Build the Rust protobuf interface
	cd proto-codegen && cargo run -- --crate-dir ../wasm-app --proto-dir ../protos

build:  ## Compile the resume data into protobuf binary
	python3 yaml-parser/build_resume.py

wasm:  ## Compile the WASM rust app
	cd wasm-app && $(MAKE) build

all: python rust build wasm  ## Run both Python & Rust codegens, build the resume, build the wasm app

pdf:  ## Create a rendered PDF of the resume based on the wasm app
	./scripts/generate_pdf.sh

serve:  ## Serve the `wasm-app` directory on port 8080
	cd wasm-app && $(MAKE) serve

deploy: python rust build wasm pdf
	cp ./wasm-app/pkg/wasm* ../craftycoder.com/static/cv/pkg
	cp ./wasm-app/pkg/bundle.js ../craftycoder.com/static/cv/pkg
	cp ./MaximeVaude-Resume.pdf ../craftycoder.com/static/cv
