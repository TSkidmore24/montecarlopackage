Package Documentation
=================

BitString class uses a numpy array to store a bitstring, a 1 dimensional array containing only 1s and 0s. This class contains
numerous methods:

''__repr__:'' Converts the bitstring into a string data type.

''__eq__:'' Comparison operator for bitstring objects. 

''__len__'' Returns the length of entrys in numpy array.

''on(self)'' Returns the number of 1s in numpy array.

''off(self)'' Returns the number of 0s in numpy array.

''flip_site(self, i)'' Flips the value of the array at a specific index. 

''int(self)'' Converts the binary representation of the bitstring into equivalent decimal value.

''set_int_config(self, s)'' Directly set the value of the bitstring (numpy array) by providing a decimal integer.

''set_config(self, s)'' Directly set the value of the bitstring (numpy array) by providing a string of 0s and 1s.