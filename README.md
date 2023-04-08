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
```

## Usage

1. Place your VASP POSCAR file in the working directory.

2. Modify the `prepare_phonon_calculation.py` script to set the supercell size for the phonon calculation. Then, run the script to generate displaced structures and the `disp.yaml` file:

## python prepare_phonon_calculation.py

3. Prepare the necessary VASP input files (INCAR, KPOINTS, POTCAR) for running the calculations on the displaced structures.

4. Update the `num_displacements` variable in the `run_vasp_phonon.py` script according to the number of displacement configurations. Adjust the VASP command and the number of processors as needed. Run the script to perform VASP calculations on the displaced structures:

## python run_vasp_phonon.py

5. Run the `collect_forces.py` script to collect forces from the VASP calculations and generate the FORCE_SETS file:

## python collect_forces.py


6. Create a Phonopy configuration file (`phonopy.conf`) to define the settings for the band structure calculation. Adjust the supercell size (DIM), mesh size (MP), and band paths (BAND) as needed:


7. Run Phonopy to calculate the force constants and the phonon band structure:

```phonopy -c POSCAR --fc FORCE_SETS --dim="2 2 2" --band="0 0 0 0.5 0.5 0 0.5 0.5 0.5 0 0 0"```

8. Run the `plot_band_structure.py` script to visualize the phonon band structure:

 


