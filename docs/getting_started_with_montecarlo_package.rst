Getting Started with Montecarlo Package
========================================

This page details how to get started with Montecarlo.

Installing Dependencies
-----------------------

Before using Montecarlo, you need to install the package. You will need to install Python to use this package.

Assuming you have Python installed (and pip), I recommend using virtual environments to manage your Python packages. See the following tutorial:

https://docs.Python.org/3/library/venv.html

Download the contents of the repository.

Next, make sure that you are on the package home directory and install the package in your Python environment using:

pip install .

Next, these dependencies will need to be manually installed from the ''requirements.txt`` file located within the docs folder. 
You can install them in your Python environment using the following command (assuming you are in docs directory)::

    pip install -r requirements.txt

The required dependencies are:

- numpy
- matplotlib
- networkx
- pytest (for testing only)

Running Tests
-------------

Once the dependencies have been installed, you can run the tests in the package directory (``montecarlo/tests``). 
Use the following command to run the tests::

    pytest

This command will execute the test suite and provide feedback on the status of the tests.
