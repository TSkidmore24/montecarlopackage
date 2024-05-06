Getting Started with Montecarlo Package
========================================

This page details how to get started with Montecarlo.

Installing Dependencies
-----------------------

Before using Montecarlo, you need to install the package. You will need to install python to use this package.

Assuming you have python installed, I recommend using virtual environments to manage your python packages. See the following tutorial:

https://docs.python.org/3/library/venv.html

Download the contents of the repoisitory.

Next, make sure that you are on the package home directory and install the package in your python environment using:

pip install .

These dependencies should be installed automatically when installing the package.

If needed, these dependencies can be manually installed from the ``docs/requirements.txt`` file. You can install them in your Python 
environment using the following command::

    pip install -r docs/requirements.txt

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
