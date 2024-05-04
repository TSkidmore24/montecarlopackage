"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo

import numpy


def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

def test_bitstring_eq_initialization():
    my_bs1 = montecarlo.BitString(8)
    my_bs2 = montecarlo.BitString(8)

    assert(len(my_bs1) == 8)
    assert(len(my_bs1) == 8)

    assert my_bs1 == my_bs2 
    #assert that bitstring is filled with 8 zeros
    assert (my_bs1.config == numpy.zeros(8, dtype=int)).all()
    assert (my_bs2.config == numpy.zeros(8, dtype=int)).all()

    #check if different size bitstring are not equal
    my_bs3 = montecarlo.BitString(7)
    assert my_bs1 != my_bs3 
    assert (my_bs3.config == numpy.zeros(7, dtype=int)).all()

    #check if different value bitstring are not equal
    my_bs4 = montecarlo.BitString(7)
    my_bs4.flip_site(6)
    assert my_bs4 != my_bs3 

def test_bitstring_int_on_off_flip():
    my_bs = montecarlo.BitString(13)
    my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])
    #5 instances of 1 in bitstring
    assert my_bs.on() == 5
    #8 instances of zero in bitstring
    assert my_bs.off() == 8
    #converting binary to decimal 
    assert my_bs.int() == 3220
    #flip first digit in bitstring from 0 to 1
    my_bs.flip_site(0)
    assert my_bs.on() == 6
    assert my_bs.off() == 7

    with pytest.raises(IndexError):
        my_bs.flip_site(-1)
        my_bs.flip_site(-17)
        my_bs.flip_site(14)
        #too large of array to map to bs dimensions
        my_bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,1])
        #right dimension, incorrect value 
        my_bs.set_config([0,2,1,0,0,1,0,0,1,0,1,0])
        my_bs.set_config([0,0,1,0,-1,1,0,0,1,0,1,0])
    #forcibly change bitstring to include a value not 0 or 1
    my_bs.config[0] = 2
    with pytest.raises(ValueError):
        #This will fail since specified index is not 0 or 1
        my_bs.flip_site(0)
    #lose a 1 because forced a change from 1 to 2 at first index (0)
    assert my_bs.on() == 5
    assert my_bs.off() == 7

    my_bs.flip_site(2)
    assert my_bs.on() == 4
    assert my_bs.off() == 8

def test_bitstring_int_config_repr():
    my_bs = montecarlo.BitString(4)
    my_bs.set_int_config(8)
    assert my_bs.int() == 8

    my_bs.set_int_config(1)
    assert my_bs.int() == 1

    #throw error if dimensions of binary representation of decimal number exceed dimensions of bitstring
    with pytest.raises(ValueError):
        my_bs.set_int_config(25)

    #show that bitstring is unmodified after error
    assert my_bs.int() == 1

    my_bs.set_int_config(0)
    my_bs2 = montecarlo.BitString(4)
    my_bs2.set_int_config(0)
    assert my_bs == my_bs2

    assert my_bs.__repr__() == '[0 0 0 0]'