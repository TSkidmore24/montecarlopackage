Getting Started
===============

This page details how to get started with montecarlo. 

The purpose of this python package is to enable users to compute thermodynamic averages
using an Ising Hamiltonian. This Ising Model contains a graph, which consists of edges 
and vertices. Each vertice represents a spin of a particle, and each edge represents 
an interaction between the particles. Each edge has a corresponding weight. Using this 
model, the Ising Hamiltonian can be used to compute various thermodynamic averages 
including magnetization, energy, heat capacity and magnetic susceptibility. 

Note that various packages need to be installed, which are listed in requirements.txt. 
Use the following command to install the dependencies within your virtual environment:

pip install -r requirements.txt