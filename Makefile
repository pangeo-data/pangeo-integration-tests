lock:
	pip-compile requirements.in --output-file requirements.txt

build:
	docker build --build-arg COMMIT_SHA=$(shell git rev-parse HEAD) -t pangeo/integration .

run-docker:
	bash run_docker.sh