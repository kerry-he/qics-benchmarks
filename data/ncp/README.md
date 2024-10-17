# Benchmark Library for Noncommutative Perspective Programs

This folder contains a library of 48 conic programs in the Conic Benchmark
Format involving the epigraph of the noncommutative perspective. We provide
further details about these problems below.


## D-optimal design

In [1, Section 4.4], a matrix perspective reformulation technique is
proposed to obtain a relaxation of the D-optimal design problem by
minimizing the trace of an operator relative entropy. We include 15
instances of these problems.

[1] D. Bertsimas, R. Cory-Wright, and J. Pauphilet, “A new perspective on
low-rank optimization,” Mathematical Programming, vol. 202, no. 1,
pp. 47–92, 2023.


## Measured relative entropy

Measured relative entropies are functions used to measure the amount of
dissimilarity between two quantum states which arise in quantum hypothesis
testing tasks. It was shown in [2, Proposition 3 and 7] how these functions
could be expressed as the solution to conic programs which optimize over
the epigraph of noncommutative perspective functions. We include 15
instances of these problems to compute the measured Renyi relative entropy
of states for two randomly generated density matrices.

[2] M. Berta, O. Fawzi, and M. Tomamichel, “On variational expressions for
quantum relative entropies,” Letters in Mathematical Physics, vol. 107,
pp. 2239–2265, 2017.


## Expectation values of equilibrium states

In quantum many-body theory, an important problem is to describe
observables in equilibrium states. In [3], it was shown how a hierarchy of
conic problems involving the epigraph of the operator relative entropy can
produce converging bounds to the expectation values of these observables.
We include 18 instances of these problems to estimate the upper and lower
bounds of these expectation values.

[3] H. Fawzi, O. Fawzi, and S. O. Scalet, “Certified algorithms for
equilibrium states of local quantum Hamiltonians,” Nature Communications,
vol. 15, no. 1, p. 7394, 2024.