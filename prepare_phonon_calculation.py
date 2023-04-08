from phonopy import Phonopy
from phonopy.structure.atoms import read_vasp
from phonopy.file_IO import write_FORCE_CONSTANTS

# Read the POSCAR file
unitcell = read_vasp("POSCAR")

# Define the supercell for the phonon calculation
supercell_matrix = [[2, 0, 0],
                    [0, 2, 0],
                    [0, 0, 2]]

# Set up the Phonopy object
phonon = Phonopy(unitcell, supercell_matrix)

# Generate displacement configurations for VASP
phonon.generate_displacements(distance=0.01)
phonon.save("disp.yaml")

# Write the displaced supercell structures as POSCAR files
for i, disp in enumerate(phonon.get_displaced_atoms()):
    with open("POSCAR-%03d" % (i + 1), "w") as f:
        f.write(str(disp))
