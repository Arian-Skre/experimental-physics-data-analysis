

									*** Acoustic Resonance Analysis — Speed of Sound Determination ***


-------------------------------------------------------------------------------------------------------

* Overview:

This experiment evaluates acoustic standing-wave behaviour in a closed–open air column and compares experimentally derived values with theoretical predictions adjusted for ambient temperature conditions following installation of a new temperature control system in the laboratory.

Two independent datasets were collected by separate observers to assess measurement consistency and reproducibility.

-------------------------------------------------------------------------------------------------------

* Objective:

The primary objective of this study is to determine the speed of sound in air under controlled laboratory environmental conditions using resonance tube methods, and to evaluate the impact of improved environmental stability (temperature and humidity regulation) on measurement accuracy.

A secondary objective is to compare classical resonance-tube results with a smartphone-based acoustic analysis system (Phyphox).

-------------------------------------------------------------------------------------------------------

* Experimental Principle:

The resonance condition for a closed–open air column is modelled as:

Dₙ = v((2n − 1) / 4f) − x₀

Where:
- Dₙ is the resonance displacement
- v is the speed of sound in air
- n is the resonance mode index
- f is the tuning fork frequency
- x₀ is the end correction term

Linearization of this relationship allows extraction of:
- slope → speed of sound
- intercept → end correction

-------------------------------------------------------------------------------------------------------

* Theoretical Model:

The temperature dependence of the speed of sound is given by:

cₛ = cₛ,0 √(T / 273.15)

Where:
- cₛ,0 = 331 m/s (reference value at 0°C)
- T is absolute temperature in Kelvin

At the experimental room temperature of 21.35°C (294.50 K), the theoretical speed of sound is approximately:

cₛ ≈ 343.9 m/s

-------------------------------------------------------------------------------------------------------

* Experimental Setup:

The experiment was conducted using:

- Resonance tube (1.0 m length, 0.004 m radius)
- Set of tuning forks across multiple frequencies
- Rubber mallet for excitation
- Phyphox mobile acoustic measurement system (for comparison dataset)

Resonance positions were identified by maximum acoustic amplitude response within the tube.

Two independent observers collected measurements:
- Observer A (author)
- Observer C (partner)

-------------------------------------------------------------------------------------------------------

* Data Structure:

The dataset contains:

- `frequency_hz`: tuning fork frequency
- `attempt`: repeated measurement index at each frequency
- `resonance_displacement_m`: measured air column length at resonance
- `experimenter`: observer identifier (A or C)
- `linearized_variable`: computed transformation (2n−1)/(4f)

-------------------------------------------------------------------------------------------------------

* Computational Workflow:

The analysis pipeline (implemented in Python) performs the following steps:

1. Load raw experimental data
2. Clean and standardize column formatting
3. Convert all physical quantities to numeric format
4. Compute linearized resonance variable:
   (2n − 1) / (4f)
5. Separate datasets by experimenter
6. Perform linear regression:
   Dₙ = v x − x₀
7. Extract:
   - speed of sound (slope)
   - end correction (intercept)
   - R² goodness-of-fit
8. Compare with theoretical prediction
9. Generate publication-style plots
10. Export processed dataset

-------------------------------------------------------------------------------------------------------

* Key Results:

 Experimental Speed of Sound

- Observer A: ~325 m/s (± uncertainty from regression)
- Observer C: ~325 m/s (± uncertainty from regression)

 Theoretical Value

- 343.9 m/s at 21.35°C

 Phyphox Measurement

- v = 359 ± 6 m/s

-------------------------------------------------------------------------------------------------------

* Interpretation:

The experimentally derived values show modest agreement with theoretical predictions. Deviations are attributed to:

- Subjective identification of resonance maxima
- Finite Q-factor of the air column
- Imperfect sealing of the movable plunger
- Non-ideal boundary conditions at the open end
- Environmental coupling effects despite improved laboratory regulation

The Phyphox-based method yields slightly higher values, consistent with known differences between direct acoustic FFT-based measurement and classical resonance tube methods.

-------------------------------------------------------------------------------------------------------

* Physical Discussion:

A closed–open air column supports only odd harmonics due to boundary constraints:

- Closed end → displacement node
- Open end → displacement antinode

For a closed–open system:
- only odd harmonics are allowed

For a closed–closed system:
- all harmonics are supported

The fundamental mode for a closed–open pipe is:

f₁ = v / (4L)

This corresponds to the lowest resonant frequency observed in the dataset (~81.5 Hz).

-------------------------------------------------------------------------------------------------------

* Tools Used:

- Python 3.13.2
- Pandas (data processing)
- NumPy (numerical computation)
- SciPy (linear regression)
- Matplotlib (visualization)

-------------------------------------------------------------------------------------------------------

* Repository Purpose:

This project demonstrates:

- structured experimental data analysis
- reproducible computational workflow
- quantitative comparison of theoretical vs experimental models
- multi-observer measurement validation
- integration of classical physics with modern sensor-based methods

--------------------------------------------------------------------------------------------------------

* Future Work:

Potential extensions include:

- uncertainty propagation analysis
- weighted regression based on measurement variance
- frequency-domain analysis of resonance peaks
- automated resonance detection from audio signals
- extension to light-wave interference experiments

--------------------------------------------------------------------------------------------------------

* License:

This repository is intended for educational and scientific demonstration purposes.

