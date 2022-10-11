BACK_SERVICE := backend
BASE_SERVICE := baseImage
ROOT_DIR := $(shell pwd)
BLUE = \033[34m
NC = \033[0m


.PHONY: help build build-base build-back run run-back down log-back gogogo lazy

help: ## Show help message
	@printf "Usage:\n"
	@printf "  make $(BLUE)<target>$(NC)\n\n"
	@printf "Targets:\n"
	@perl -nle'print $& if m{^[a-zA-Z0-9_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ":.*?## "}; \
		{printf "$(BLUE)  %-18s$(NC) %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

# QUICK START
gogogo: build run ## Quick start

lazy: build-back  run

# DOCKER TASKS
## build
build: build-base build-back  ## Build the container

build-base: ## Build backend base image
	docker-compose build --force-rm --no-cache $(BASE_SERVICE)

build-back: ## Build backend image
	docker-compose build --force-rm --no-cache $(BACK_SERVICE)

## run
run: down run-back ## Run container

run-back: ## Run backend container
	docker-compose up -d $(BACK_SERVICE)

## down
down:	## Down container
	docker-compose down

## log
log-back: ## Log backend 
	docker-compose logs -f --tail 100 $(BACK_SERVICE)