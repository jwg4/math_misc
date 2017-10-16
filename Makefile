all: spaced_pi.txt hints.txt

spaced_pi.txt: pi.txt spacing.py
	python spacing.py > $@

hints.txt: pi.txt triplets.txt make_hints.py success_number
	python make_hints.py > $@

success_number: success_log.txt measure_success.py
	python measure_success.py > $@

test:
	python -m unittest discover
