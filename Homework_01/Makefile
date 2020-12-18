build:
	docker build . -t homework01:latest

stop:
	docker stop hw1

start:
	docker run --rm -it --name hw1 homework01:latest

delete:
	docker rm -f hw1

setup: build start