# Benchmark Library for Semidefinite Programs

This folder contains a library of 49 semidefinite programs in the SDPLIB
sparse format from applications arising from quantum information theory.
We include two versions of this library of problems:

- ``./real/`` contains formulations of these SDPs, where complex-valued
  SDPs are reformulated as a real-valued SDP using the technique discussed
  [here](https://docs.mosek.com/modeling-cookbook/sdo.html#hermitian-matrices),
- ``./complex/`` contains formulations of these SDPs, where complex-valued
  SDPs are kept as complex-valued SDPs.

We provide further details about these problems below.


## Quantum state discrimination

We design a set of POVMs which maximize the probability of successfully
identifying a given set of quantum states. We include

- 3 minimum-error quantum state discrimination problems (see 
  [1, Section 4.2.1]),
- 1 unambiguous state discrimination problem (see [1, Section 4.2.4]).

[1] P. Skrzypczyk and D. Cavalcanti, Semidefinite Programming in Quantum
Information Science. IOP Publishing, 2023.


## Quantum state fidelity

The quantum state fidelity $F(X, Y)=\| \sqrt{X}\sqrt{Y} \|_1^2$ is used to
measure how similar two quantum states are, and can be computed using a
semidefinite program [2, Section 2.1]. We estimate this for 6 randomly
generated pairs of quantum states.

[2] J. Watrous, “Simpler semidefinite programs for completely bounded
norms,” arXiv preprint arXiv:1207.5726, 2012.


## Diamond norm

The diamond norm is used to measure the dissimilarity between two quantum
channels. This can be computed as the semidefinite program described in
[2, Section 3.2]. We estimate this for 6 randomly generated quantum
channels.


## Quantum optimal transport

We consider the quantum analog of the optimzal transport problem [3], which
minimizes a linear objective function of a bipartite density matrix subject
to constraints on its reduced states. We consider 3 of these problems for
randomly generated reduced states.

[3] S. Cole, M. Eckstein, S. Friedland, and K. Zyczkowski, “On quantum
optimal transport,” Mathematical Physics, Analysis and Geometry, vol. 26,
no. 2, p. 14, 2023.


## DPS hierarchy

Determining whether a given quantum state is entangled or separable is 
NP-hard in general. The Doherty-Parrilo-Spedalieri hierarchy provides
a hierarchy of linear matrix inequalities which must be satisfied by all
separable states, which we can use to check if a state is separable or
entangled (see [4, Section 7]). We solve this problem for:

- 4 randomly generated entangled quantum states,
- 4 randomly generated separable quantum states.

[4] V. Siddhu and S. Tayur, “Five starter pieces: Quantum information science
via semidefinite programs,” in Tutorials in Operations Research: Emerging
and Impactful Topics in Operations. INFORMS, 2022, pp. 59–92.


## NPA hierarchy

The Navascues-Pironio-Acin hierarchy [50, 51] solves non-commutative
polynomial optimization problems by constructing a hierarchy of
semidefinite programs which lower bound the optimal value. We obtain
problems using Moment [5], and include:

- 3 bounds for the CHSH inequality,
- 3 bounds for the I3322 inequality,
- 2 bounds for the Brown-Fawzi-Fawzi calculation of the quantum conditional
  entropy. 

[5] A. J. Garner and M. Ara´ujo, “Introducing Moment: A toolkit for
semi-definite programming with moment matrices,” arXiv preprint
arXiv:2406.15559, 2024.


## Quantum relative entropy

In [6], it was shown how the quantum relative entropy could be 
approximated using linear matrix inequalities. We use this technique to
solve 7 instances of a toy quantum relative entropy program.

[6] H. Fawzi, J. Saunderson, and P. A. Parrilo, “Semidefinite
approximations of the matrix logarithm,” Foundations of Computational
Mathematics, vol. 19, pp. 259–296, 2019.


## Quantum chemistry

In [7, 8], it was shown how the potential energy surfaces of molecules
could be calculated by solving a semidefinite program. We include 7
instances of these problems taken from 
[here](https://plato.asu.edu/ftp/sdp/).

[7] M. Nakata, H. Nakatsuji, M. Ehara, M. Fukuda, K. Nakata, and K.
Fujisawa, “Variational calculations of fermion second-order reduced density
matrices by semidefinite programming algorithm,” The Journal of Chemical
Physics, vol. 114, no. 19, pp. 8282–8292, 2001.

[8] M. Nakata, M. Ehara, and H. Nakatsuji, “Density matrix variational
theory: Application to the potential energy surfaces and strongly
correlated systems,” The Journal of Chemical Physics, vol. 116, no. 13,
pp. 5432–5439, 2002.