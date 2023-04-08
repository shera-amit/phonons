import matplotlib.pyplot as plt
from phonopy.file_IO import parse_band_yaml

# Read band structure from band.yaml
bands, q_points, distance = parse_band_yaml(filename="band.yaml")

# Plot the band structure
fig, ax = plt.subplots()
for band in bands:
    ax.plot(distance, band, color="black", linewidth=1)

ax.set_xlabel("Wave vector")
ax.set_ylabel("Frequency (THz)")
plt.xticks(distance[::20], ["$\Gamma$", "X", "M", "$\Gamma$"])
plt.show()
