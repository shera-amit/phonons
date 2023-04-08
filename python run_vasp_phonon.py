import os
import subprocess

# Replace N with the number of displacement configurations
num_displacements = N

# Copy necessary VASP input files (INCAR, KPOINTS, POTCAR) to each displacement directory
for i in range(1, num_displacements + 1):
    disp_dir = f"disp-{i:03d}"
    os.makedirs(disp_dir)
    for filename in ["INCAR", "KPOINTS", "POTCAR"]:
        subprocess.run(["cp", filename, disp_dir])
    subprocess.run(["cp", f"POSCAR-{i:03d}", os.path.join(disp_dir, "POSCAR")])

# Run VASP for each displacement directory
for i in range(1, num_displacements + 1):
    disp_dir = f"disp-{i:03d}"
    os.chdir(disp_dir)
    
    # Adjust the VASP command and number of processors as needed
    vasp_command = ["mpirun", "-np", "8", "vasp"]
    subprocess.run(vasp_command)
    
    os.chdir("..")
