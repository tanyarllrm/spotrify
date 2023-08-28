
fmt:
	@poetry run black .

fmtcheck:
	@poetry run black . --check --diff --color

lint:
	@poetry run flake8 --color always

test:
	@poetry run pytest -vv

run:
	@poetry run python main.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: help
.DEFAULT_GOAL := help
