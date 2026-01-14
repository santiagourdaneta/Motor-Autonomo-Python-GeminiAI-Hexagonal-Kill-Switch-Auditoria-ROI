.PHONY: install lint test run smoke chaos

install:
	pip install -r requirements.txt
	pre-commit install

lint:
	ruff check . --fix
	ruff format .

test:
	PYTHONPATH=. pytest

smoke:
	PYTHONPATH=. pytest tests/smoke_test.py

chaos:
	PYTHONPATH=. python tests/test_kill_switch.py

run:
	python main.py
