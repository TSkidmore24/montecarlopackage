Getting Started with Montecarlo Package
===============

This page details how to get started with montecarlo. 

The purpose of this python package is to enable users to compute thermodynamic averages
using an Ising Hamiltonian. This Ising Model contains a graph, which consists of edges 
and vertices. Each vertice represents a spin of a particle, and each edge represents 
an interaction between the particles. Each edge has a corresponding weight. Using this 
model, the Ising Hamiltonian can be used to compute various thermodynamic averages 
including magnetization, energy, heat capacity and magnetic susceptibility. 

Note that various additional packages need to be installed, including:

numpy
matplotlib
networkx

These dependencies are listed in the directory docs/requirements.txt:

pip install -r docs/requirements.txt