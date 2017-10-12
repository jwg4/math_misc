all: spaced_pi.txt hints.txt

spaced_pi.txt: pi.txt spacing.py
	python spacing.py > $@

hints.txt: pi.txt triplets.txt make_hints.py 
	python make_hints.py > $@

test:
	python -m unittest discover
