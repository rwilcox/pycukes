all: install test

install:
	@python2.5 setup.py install

test:
	@python2.5 src/specs/run_tests.py
