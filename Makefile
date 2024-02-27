up:
	docker-compose up

build:
	docker-compose up --build

down:
	docker-compose down

sh: 
	docker-compose run --rm app sh