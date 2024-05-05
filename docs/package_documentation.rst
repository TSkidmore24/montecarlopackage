Package Documentation
=====================

BitString Class
---------------

The `BitString` class uses a numpy array to store a bitstring, which is a 1-dimensional array containing only 1s and 0s.

.. autoclass:: BitString
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

Method Details
--------------

__repr__
^^^^^^^^

Converts the bitstring into a string data type.

__eq__
^^^^^^

Comparison operator for bitstring objects.

__len__
^^^^^^^

Returns the length of entries in the numpy array.

on()
^^^

Returns the number of 1s in the numpy array.

off()
^^^^

Returns the number of 0s in the numpy array.

flip_site(i)
^^^^^^^^^^^^

Flips the value of the array at a specific index.

int()
^^^^

Converts the binary representation of the bitstring into the equivalent decimal value.

set_int_config(s)
^^^^^^^^^^^^^^^^

Directly sets the value of the bitstring (numpy array) by providing a decimal integer.

set_config(s)
^^^^^^^^^^^^^

Directly sets the value of the bitstring (numpy array) by providing a string of 0s and 1s.
