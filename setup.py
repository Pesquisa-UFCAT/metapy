from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
    	name = 'metapy_toolbox',
		long_description=long_description,
		long_description_content_type="text/markdown",
    	version = '2024.3.1',
		url = 'https://wmpjrufg.github.io/METAPY/',
    	license = 'MIT',
    	author_email = 'wanderlei_junior@ufcat.edu.br',
    	packages = ['metapy_toolbox'],
    	description = "The METApy optimization toolbox is an easy-to-use environment for applying metaheuristic optimization methods. The platform has several optimization methods and functions for generating charts and statistical analysis of the results.",
    	classifiers = ["Programming Language :: Python","Topic :: Scientific/Engineering :: Mathematics", "Topic :: Scientific/Engineering"],
    	install_requires = ["numpy", "pandas", "tqdm"]
     )

# pip install setuptools
# python setup.py bdist_wheel
# pip install twine
# twine upload --repository testpypi dist/*
# twine upload dist/*