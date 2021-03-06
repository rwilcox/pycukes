import doctest
import unittest
import os


if __name__ == '__main__':
    THIS_DIR = os.path.dirname(__file__) or '.'
    suite = unittest.TestSuite()
    for file in os.listdir(THIS_DIR):
        if file.endswith('.py') and file not in ['__init__.py', 'run_specs.py']:
            suite.addTest(doctest.DocTestSuite(__import__(file[:-3]),
                                               optionflags=doctest.ELLIPSIS))
    runner = unittest.TextTestRunner()
    runner.run(suite)
