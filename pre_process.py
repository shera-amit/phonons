import os
import shutil
import subprocess
import time

# Create the supercell using phonopy
subprocess.run(["phonopy", "-d", "--dim=2 2 2"])

# List all files in the current directory
files = os.listdir()

# Filter the list to keep only the POSCAR files
poscar_files = [f for f in files if f.startswith('POSCAR-')]

# Loop through the POSCAR files, create directories, and copy the files
for poscar_file in poscar_files:
    dir_name = f"disp-{poscar_file.split('-')[1]}"

    # Create the directory and copy the POSCAR file
    os.makedirs(dir_name, exist_ok=True)
    shutil.copy(poscar_file, os.path.join(dir_name, "POSCAR"))

    # Copy the run.py script to the directory
    shutil.copy("run.py", os.path.join(dir_name, "run.py"))

    # Copy the vasp_job.slurm script to the directory
    shutil.copy("submit.sh", os.path.join(dir_name, "submit.sh"))

    # Submit the sbatch script in the corresponding directory
    subprocess.run(["sbatch", "submit.sh"], cwd=dir_name)

