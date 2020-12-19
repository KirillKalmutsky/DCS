build:
	docker build . -t homework01:latest

stop:
	docker stop hw1

run:
	docker run --rm -it --name hw1 homework01:latest

delete:
	docker rmi -f homework01

setup: build run