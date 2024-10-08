# Benchmark Library for Quantum Relative Entropy Programs

This folder contains a library of 144 quantum relative entropy programs in
the Conic Benchmark Format. We include two versions of this library of
problems:

- ``./qre/`` contains formulations of these QREPs using only the quantum
  relative entropy cone,
- ``./qics/`` contains formulations of these QREPs using the full suite of
  cones supported by QICS, including the quantum conditional entropy cone
  and quantum key distribbution cone.

We provide further details about these problems below.


## Nearest correlation matrix

We compute the closest correlation matrix to a given matrix, in the quantum
relative entropy sense (see, [1, Section 8.1]) for:

- 5 randomly generated full rank matrices,
- 5 randomly generated rank one matrices.

We also compute the closest tridiagonal correlation matrix to a given
matrix for:

- 5 randomly generated full rank matrices,
- 5 randomly generated rank one matrices.

[1] M. Karimi and L. Tuncel, “Efficient implementation of interior-point
methods for quantum relative entropy,” arXiv preprint arXiv:2312.07438,
2023.


## Relative entropy of entanglement

We quantify how entangled a given bipartite quantum state is by estimating
the distance between the matrix and the set of matrices satisfying the
positive partial transpose criteria (see [2, Section 4]). We compute this
for

- 7 randomly generated full rank input states,
- 7 randomly generated rank one input states.

[2] H. Fawzi and O. Fawzi, “Efficient optimization of the quantum relative
entropy,” Journal of Physics A: Mathematical and Theoretical, vol. 51, no.
15, p. 154003, 2018.


## Quantum channel capacities

Quantum channel capacities quantify the maximum amount of information we
can transit through a noisy quantum channel. Our library includes:

- 6 classical-quantum channel capacities of randomly generated channels 
  (see [4, Section 3.3.1]),
- Entanglement-assisted channel capacities (see [3, Section 8.4.4]) for
    - 10 randomly generated channels,
    - 10 degenerate amplitude damping channels,
- 10 quantum-quantum channel capacities of randomly generated degradable
  channels (see [4, Section 3.3.2]).

[3] C. Coey, L. Kapelevich, and J. P. Vielma, “Conic optimization with 
spectral functions on Euclidean Jordan algebras,” Mathematics of Operations
Research, vol. 48, no. 4, pp. 1906–1933, 2023.

[4] K. He, J. Saunderson, and H. Fawzi, “Exploiting structure in quantum
relative entropy programs,” arXiv preprint arXiv:2407.00241, 2024.


## Quantum rate distortion

The quantum rate distortion function characterizes the minimum amount of
information required to compress and transmit a quantum information source
through a quantum channel without exceeding a given distortion threshold
(see [4, Section 3.2]). We compute the optimal rate-distortion tradeoff for

- 5 randomly generated full rank input states for $D=0.5$,
- 5 randomly generated rank one input states for $D=0$.

Additionally, we also include problems reduced using the symmetry reduction
technique from [5] to compute the optimal rate-distortion tradeoff for

- 6 randomly generated full rank input states for $D=0.5$,
- 6 randomly generated rank one input states for $D=0$.

[5] K. He, J. Saunderson, and H. Fawzi, “Efficient computation of the
quantum rate-distortion function,” Quantum, vol. 8, p. 1314, Apr. 2024.


## Quantum key rates

The quantum key rate is a quantity which characterizes the security of
a given quantum protocol. We include quantum key rates for the following
protocols:

- From [6] (see, also, https://github.com/araujoms/ConicQKD.jl), we include
    - 4 noisy DMCV protocols,
    - 2 noiseless DMCV protocols,
    - 9 noiseless DMCV protocols which use the facial reduction technique
      from [7],
    - 9 overlapping bases protocols,
    - 8 MUB protocols using $d+1$ MUBs,
    - 8 MUB protocols using $2$ MUBs.
- From [7] (see, also, [here](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/ZGNQKDmainsolverUSEDforPUBLCNJuly31/)), 
  we include
    - 5 examples which do not use facial reduction,
    - 4 examples which use the facial reduction technique from [7].

[6] H. Hu, J. Im, J. Lin, N. Lutkenhaus, and H. Wolkowicz, “Robust
interior point method for quantum key distribution rate computation,”
Quantum, vol. 6, p. 792, 2022.

[7] A. G. Lorente, P. V. Parellada, M. Castillo-Celeita, and M. Ara´ujo,
“Quantum key distribution rates from non-symmetric conic optimization,”
arXiv preprint arXiv:2407.00152, 2024.


## Ground state energy of Hamiltonians

We lower bound the ground energy of a Hamiltonian using the method in [8]
by solving a quantum relative entropy program. We include 6 instances of
this problem corresponding to $L=2$ to $L=7$.

[8] H. Fawzi, O. Fawzi, and S. O. Scalet, “Entropy constraints for ground 
energy optimization,” Journal of Mathematical Physics, vol. 65, no. 3, 
2024.
