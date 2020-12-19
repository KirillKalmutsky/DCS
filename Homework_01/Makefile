build:
	docker build . -t homework01:latest

stop:
	docker stop hw1

run_docker:
	docker run --rm -it --name hw1 homework01:latest

run:
	python3 app.py

delete:
	docker rmi -f homework01:latest

setup: build run_docker