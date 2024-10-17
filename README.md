# Benchmark Library for QICS

This repository includes benchmark libraries for semidefinite programs, 
quantum relative entropy programs, and conic programs involving epigraphs
of noncommutative perspective functions, which were used to evaluate the
performance of QICS.

To run QICS against these problems, you should first install QICS from pip
by calling

```bash
pip install qics
```

then clone this repository

```bash
git clone https://github.com/kerry-he/qics-benchmarks.git
```

You can then use the ``run_benchmarks.py`` script to run QICS against all
problems in a given folder. For example, the following lines will run QICS
against the library of quantum relative entropy programs.

```bash
cd qics-benchmarks
python run_benchmarks.py -d data/qrep/qics
```

This outputs a CSV file named ``qics_benchmarks_*.csv`` into the working
directory which contains a summary of the solver outputs from QICS.