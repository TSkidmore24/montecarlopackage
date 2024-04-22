"""
MonteCarlo
Introduction to the Monte Carlo method
"""
import sys
from setuptools import setup, find_packages


# Read in requirements.txt
requirements = open('./docs/requirements.txt').readlines()
requirements = [r.strip() for r in requirements]
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    name='montecarlopackage',
    author='Tommy',
    author_email='skidmore2024@vt.edu',
    license='MIT',

    packages=find_packages(),

    include_package_data=True,

    setup_requires=[] + pytest_runner,

    install_requires=requirements
)