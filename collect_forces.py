import numpy as np
from phonopy import Phonopy
from phonopy.structure.atoms import read_vasp
from phonopy.file_IO import parse_FORCE_SETS, write_FORCE_SETS

# Read the POSCAR file
unitcell = read_vasp("POSCAR")

# Define the supercell for the phonon calculation
supercell_matrix = [[2, 0, 0],
                    [0, 2, 0],
                    [0, 0, 2]]

# Set up the Phonopy object
phonon = Phonopy(unitcell, supercell_matrix)
phonon.load("disp.yaml")

# Collect forces from VASP calculations
forces = []
for i, _ in enumerate(phonon.get_displaced_atoms()):
    force_file = "disp-%03d/vasprun.xml" % (i + 1)
    force_set = parse_FORCE_SETS(filename=force
    force_file = "disp-%03d/vasprun.xml" % (i + 1)
    force_set = parse_FORCE_SETS(filename=force_file)
    forces.append(force_set)

forces = np.array(forces)

# Write the FORCE_SETS file
write_FORCE_SETS(phonon.get_displacement_dataset(), forces=forces)
