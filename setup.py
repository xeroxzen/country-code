import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name= "pycountrycode",
    version="1.1.1",
    description="A neat country call code retriever",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xeroxzen/pycountrycode",
    author="Andile Mbele",
    author_email="andilembele020@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers and Enthusiasts",
		"Natural Language :: English",
    ],
    packages=["countrycode"],
    include_package_data=True,
    install_requires=[],
)
