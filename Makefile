all: spaced_pi.txt

spaced_pi.txt: pi.txt spacing.py
	python spacing.py > $@

test:
	python -m unittest discover
