# Naive implementations of Lattice-based Signature Schemes

## Description
This repository contains naive implementations of two key lattice-based signature schemes, pivotal in cryptographic applications. These implementations serve as a resource for understanding the practical aspects of lattice cryptography.

## Implementations
- Lattice Signature without Trapdoors: Utilizes a unimodal discrete Gaussian distribution. Based on Lyubashevsky's 2012 paper.
- Lattice Signature with Bimodal Discrete Gaussian: Follows the approach proposed by Ducas and Lyubashevsky in 2013.

## Prerequisites
- Install [python2.7](https://www.python.org/downloads/release/python-2716/)
- Install [SageMath](https://www.sagemath.org/) using this [guide](https://doc.sagemath.org/html/en/installation/index.html)

## Usage
```sh
# bliss.py
python bliss.py

# lyu12vS.py
python lyu12vS.py

# sampler.py 
python sampler.py
```

## License
This project is licensed under the MIT License.

## Acknowledgments
 - Lattice signature without trapdoors using unimodal discrete Gaussian (Lyubashevsky, 2012)
 - Lattice signature using bimodal discrete Gaussian (Ducas, Lyubashevsky, et. al., 2013)
