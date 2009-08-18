from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pycukes',
      version=version,
      description="A Cucumber-like BDD framework built on top of Pyhistorian",
      long_description=open('README.rst').read(),
      classifiers=[ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Testing',],
      keywords='bdd behaviour behavior pyhistorian story',
      author='Hugo Lopes Tavares',
      author_email='hltbra@gmail.com',
      url='http://github.com/hugobr/pycukes',
      license='MIT License',
      packages=['pycukes', 'pycukes.tests', 'pycukes.tests.scenarios',],
      package_dir={'pycukes': 'src',  'pycukes.tests': 'src/tests', 'pycukes.tests.scenarios': 'src/tests/scenarios'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'story_parser',
          'pyhistorian',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
