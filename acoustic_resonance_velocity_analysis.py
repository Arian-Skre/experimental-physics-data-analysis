import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
pd.set_option("display.float_format", "{:.6f}".format)

# ============================================================
# Acoustic Resonance Analysis
# Determination of the Speed of Sound in Air
# ============================================================

os.makedirs("graphs", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Load raw data

df = pd.read_csv("sound_wave_resonance_data.csv")

df.columns = df.columns.str.strip()

df = df.rename(columns={
    "frequency (hz)": "frequency_hz",
    "n": "attempt",
    "dn_m": "resonance_displacement_m",
    "observer": "experimenter",
    "calc_value": "linearized_variable"
})

for col in ["frequency_hz", "attempt", "resonance_displacement_m"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=[
    "frequency_hz",
    "attempt",
    "resonance_displacement_m"
])

print(df.head(10))
print(len(df))

# OPTIONAL:
# Recalculate linearized variable for reproducibility
# x = (2n - 1) / (4f)

df["linearized_variable"] = (
    (2 * df["attempt"] - 1)
    / (4 * df["frequency_hz"])
)

# Separate datasets by experimenter

df_A = df[df["experimenter"] == "A"]
df_C = df[df["experimenter"] == "C"]

# Perform linear regression
# D_n = v*x - x_0

fit_A = linregress(
    df_A["linearized_variable"],
    df_A["resonance_displacement_m"]
)

fit_C = linregress(
    df_C["linearized_variable"],
    df_C["resonance_displacement_m"]
)

# Extract regression parameters

slope_A = fit_A.slope
intercept_A = fit_A.intercept
rvalue_A = fit_A.rvalue
stderr_A = fit_A.stderr
intercept_stderr_A = fit_A.intercept_stderr

slope_C = fit_C.slope
intercept_C = fit_C.intercept
rvalue_C = fit_C.rvalue
stderr_C = fit_C.stderr
intercept_stderr_C = fit_C.intercept_stderr

# Print regression summaries

print("\n================================================")
print("EXPERIMENTER A")
print("================================================")

print(f"Speed of sound (slope): {slope_A:.2f} ± {stderr_A:.2f} m/s")

print(
    f"End correction (intercept): "
    f"{intercept_A:.5f} ± {intercept_stderr_A:.5f} m"
)

print(f"R² value: {rvalue_A**2:.5f}")

print("\n================================================")
print("EXPERIMENTER C")
print("================================================")

print(f"Speed of sound (slope): {slope_C:.2f} ± {stderr_C:.2f} m/s")

print(
    f"End correction (intercept): "
    f"{intercept_C:.5f} ± {intercept_stderr_C:.5f} m"
)

print(f"R² value: {rvalue_C**2:.5f}")

# Theoretical speed of sound
# v = 331 + 0.6T

temperature_c = 21.35

v_theoretical = 331 + 0.6 * temperature_c

print("\n================================================")
print("THEORETICAL COMPARISON")
print("================================================")

print(f"Theoretical speed of sound: {v_theoretical:.2f} m/s")

# Generate best-fit lines

xfit = np.linspace(
    df["linearized_variable"].min(),
    df["linearized_variable"].max(),
    500
)

yfit_A = slope_A * xfit + intercept_A
yfit_C = slope_C * xfit + intercept_C

# Create plot

plt.figure(figsize=(10, 6))

# Scatter data
plt.scatter(
    df_A["linearized_variable"],
    df_A["resonance_displacement_m"],
    label="Experimenter A Data"
)

plt.scatter(
    df_C["linearized_variable"],
    df_C["resonance_displacement_m"],
    label="Experimenter C Data"
)

# Best-fit lines
plt.plot(
    xfit,
    yfit_A,
    label=f"A Fit: v = {slope_A:.1f} m/s"
)

plt.plot(
    xfit,
    yfit_C,
    label=f"C Fit: v = {slope_C:.1f} m/s"
)

# Labels
plt.xlabel(r'$(2n - 1)/(4f)$ (s/m)')
plt.ylabel(r'$D_n$ (m)')

plt.title(
    "Linearized Resonance Data for "
    "Determination of the Speed of Sound"
)

plt.legend()
plt.grid(True)

# Save graph

plt.savefig(
    "graphs/resonance_regression.png",
    dpi=300,
    bbox_inches="tight"
)

# Save processed data

df.to_csv("processed_data.csv", index=False)

# Completion message

print("\n================================================")
print("FILES GENERATED")
print("================================================")

print("Processed data saved to:")
print("processed_data.csv")

print("\nGraph saved to:")
print("graphs/resonance_regression.png")

print("\nAnalysis complete.")

print(df.dtypes)
print(df.head())
df.to_csv("processed_data.csv", index=False, float_format="%.6f")
