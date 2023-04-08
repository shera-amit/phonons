# Phonon Calculations with Phonopy and VASP

This repository provides a set of Python and shell scripts for performing phonon calculations using Phonopy and VASP. The workflow consists of the following steps:

1. Prepare the necessary input files for VASP.
2. Run VASP calculations on displaced structures.
3. Collect forces and generate the FORCE_SETS file.
4. Calculate the force constants and the phonon band structure.
5. Plot the phonon band structure.

## Prerequisites

- [VASP](https://www.vasp.at/) (properly installed and configured on your system)
- [Phonopy](https://phonopy.github.io/phonopy/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

Install the required Python packages using pip:

```bash
pip install phonopy numpy matplotlib
