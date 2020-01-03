#! usr/bin/env python
# -*- coding: utf-8 -*-


'''The setup.py file'''

import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	author='Andile Mbele',
	author_email='andilembele020@gmail.com',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating :: OS Independent',
		'Intended Audience :: Developers and Enthusiasts',
		'Natural Language :: English'
	],
	name='pycountrycode',
	packages=setuptools.find_packages(),
	description='A neat country call code retriever',
	long_description_content_type='text/markdown',
	url='https://github.com/Andile-Mbele/pycountrycode',
	install_requires=requirements,
	license='MIT license',
	keywords='pycountrycode',
	setup_requires=setup_requirements,
	version='1.0.1',
)
