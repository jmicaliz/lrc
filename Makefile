.DEFAULT_GOAL := help

all: format clean docs install-deps init help requirements validate test test-debug

.PHONY: help all

help: ## generate make help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

format: ## sort imports and paint it black
	isort --settings pyproject.toml .
	black --config pyproject.toml .
	flake8 --config .flake8 src/

lock: # Creates poetry.lock file
	poetry cache clear --all . -n
	poetry lock --no-update -vvv

update: # Updates poetry.lock file with up-to-date dependencies
	poetry cache clear --all . -n
	poetry update -vvv

install-deps: ## install python requirements
	poetry install --remove-untracked -vv

init: install-deps ## initialize project with dependencies and pre-commit hooks
	pre-commit install

validate:  ## run pre-commit validation
	pre-commit run --all-files
