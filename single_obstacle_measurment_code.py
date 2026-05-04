
# Single-Obstacle Diffraction Measurement Study
# Automated Optical Diffraction Analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CONSTANTS

LAMBDA = 532e-9  # meters

L = 0.90  # meters

# LOAD DATA

df = pd.read_csv("light_diffraction_data.csv")
df.columns = df.columns.str.strip()

# CALCULATE sin(theta)
# Geometry:
# sin(theta) = x / sqrt(x^2 + L^2)

df["sin_theta"] = df["x"] / np.sqrt(df["x"]**2 + L**2)

# CALCULATE HAIR WIDTH

# Diffraction equation:
# w = m * lambda / sin(theta)

df["width_m"] = (df["m"] * LAMBDA) / df["sin_theta"]

# STATISTICS

mean_width = df["width_m"].mean()
std_width = df["width_m"].std()

# PRINT RESULTS

print("\n================================================")
print(" SINGLE-OBSTACLE DIFFRACTION ANALYSIS")
print("================================================\n")

print(df)

print("\n------------------------------------------------")
print(f"Average Hair Width: {mean_width:.4e} m")
print(f"Standard Deviation: {std_width:.4e} m")
print(f"Approximate Width: {mean_width * 1e6:.2f} micrometers")
print("------------------------------------------------\n")

# PLOT 1
# Diffraction Minimum Order vs Fringe Position

plt.figure(figsize=(8, 5))

plt.plot(df["m"], df["x"], marker='o')

plt.xlabel("Diffraction Minimum Order (m)")
plt.ylabel("Fringe Position x (m)")
plt.title("Diffraction Minimum Order vs Fringe Position")

plt.grid(True)

plt.tight_layout()

plt.savefig("diffraction_order_plot.png", dpi=300)

# PLOT 2
# Calculated Hair Width vs Diffraction Order

plt.figure(figsize=(8, 5))

plt.plot(df["m"], df["width_m"] * 1e6, marker='o')

plt.axhline(
    mean_width * 1e6,
    linestyle='--',
    label=f"Mean Width = {mean_width * 1e6:.2f} μm"
)

plt.xlabel("Diffraction Minimum Order (m)")
plt.ylabel("Calculated Hair Width (μm)")
plt.title("Calculated Hair Width vs Diffraction Order")

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("hair_width_plot.png", dpi=300)

# EXPORT ANALYZED DATA

df.to_csv("light_diffraction_analysis_output.csv", index=False)

print("Generated Files:")
print(" - diffraction_order_plot.png")
print(" - hair_width_plot.png")
print(" - light_diffraction_analysis_output.csv")
print("\nAnalysis complete.")
