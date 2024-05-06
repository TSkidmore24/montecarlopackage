Package Documentation
=====================

BitString Class
---------------

The `BitString` class uses a numpy array to store a bitstring, which is a 1-dimensional array containing only 1s and 0s.

.. autoclass:: BitString
   :members:
   :undoc-members:
   :show-inheritance:

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


IsingHamiltonian Class
----------------------

The `IsingHamiltonian` class defines an Ising Hamiltonian.

For a graph, defined by a set of edges and vertices, we want to represent an Ising model, where the edge weights are given by the spin interactions.

Given a configuration of spins, we can define the energy using what is referred to as an Ising Hamiltonian:

H = sum(J(ij)s(i)s(j))

The Hamiltonian is a sum over all edges in the graph, with J(ij) representing the edge weights associated with each spin interaction.
s(i) takes a value of 1 if the spin is 'up' and -1 if it is 'down'.

**Note:** As we saw before, this Hamiltonian operator is simple, in that a single `BitString` returns a single energy.



.. autoclass:: IsingHamiltonian
   :members:
   :undoc-members:
   :show-inheritance:


   
Method Details
--------------

__init__
^^^^^^^^

Converts an ising graph into a list of tuples. 

energy(bitstring, graph)
^^^^^^^^^^^^^^^^^^^^^^^^

Computes the energy associated with a specific configuration (represented as a bitstring).

compute_average_values(bitstring, graph, temperature)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Computes the average energy, magnetization, heat capacity, and mangetic susceptibility for the Ising graph. 

get_lowest_energy_config(self)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Computers the lowest energy configuration for a length of bitstring.

