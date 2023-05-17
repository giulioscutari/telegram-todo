format:
	python3 -m autopep8 -r --in-place .
	python3 -m black .

check:
		python3 -m autopep8 -rdv .

test:
	python3 -m coverage run --source=. -m pytest
	python3 -m coverage html
	python3 -m coverage report