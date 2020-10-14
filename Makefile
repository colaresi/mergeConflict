#! /usr/bin/env make

msgSum: addMessages.py vector.py
	python addMessages.py


.PHONY: TEST

TEST: vector.py
	./runTests.sh

