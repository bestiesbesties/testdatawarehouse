from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Tutorial voor de Hogeschool Rotterdam'
LONG_DESCRIPTION = 'Een library gemaakt voor de les in week 47.'

# Setting up
setup(
    name="hrfmp",
    version=VERSION,
    author="Leyton Sijpkens",
    author_email="1061024@hr.nl",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas','request'],
    keywords=['python', 'school', 'financial sector'],
    classifiers=[
        "Development Status :: 3 - Release",
        "Intended Audience :: Students",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)