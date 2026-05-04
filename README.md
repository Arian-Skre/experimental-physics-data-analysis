

										*** Single-Obstacle Diffraction Measurement Study ***


-------------------------------------------------------------------------------------------------------

* Overview:

	This study investigates optical diffraction produced when coherent laser light interacts with a microscopic obstacle. A green laser was directed around a human hair, producing a measurable diffraction pattern on a projection screen. By analyzing the geometry of the diffraction minima, the width of the hair was quantitatively determined.
The experiment also served as an evaluation of newly introduced laboratory laser systems, assessing their suitability for precision optical measurements and diffraction-based analysis.
The computational analysis pipeline automates the calculation of diffraction angles, obstacle width determination, statistical analysis, and graphical visualization using Python.

-------------------------------------------------------------------------------------------------------

* Experimental Objective:

The primary objective of this experiment was to:
- evaluate the performance and precision of newly acquired laboratory laser systems
- investigate single-obstacle optical diffraction behaviour
- determine the width of a human hair using diffraction geometry
- verify theoretical wavelength-dependent diffraction relationships

-------------------------------------------------------------------------------------------------------

* Physical Principles: 

The experiment is based on the wave nature of light and the formation of diffraction minima when coherent monochromatic light encounters an obstacle.
Core principles involved include:
- optical diffraction
- wave interference
- monochromatic light propagation
- angular diffraction geometry
- wavelength-dependent fringe spacing
- diffraction minima formation
The governing diffraction relationship is:

\omega = \frac{m \lambda}{sin(\theta)}

where:

\omega = obstacle width

m = diffraction minimum order

\lambda = laser wavelength

\theta = diffraction angle

Fringe spacing dependence on wavelength follows:

y \propto \lambda

-------------------------------------------------------------------------------------------------------

* Experimental Setup:

Equipment
- green laser source (532 nm)
- human hair obstacle
- white projection screen
- metric measurement scale
- fixed optical geometry arrangement

Setup Description:

	A coherent green laser beam was directed toward a suspended human hair. The resulting diffraction pattern was projected onto a white screen positioned at a known distance from the obstacle. The positions of multiple diffraction minima were measured relative to the central maximum.
These measurements were used to calculate diffraction angles and determine the width of the obstacle through diffraction analysis.

-------------------------------------------------------------------------------------------------------

* Data Acquisition Procedure:

The experimental procedure consisted of:
- Aligning the laser with the human hair obstacle
- Projecting the diffraction pattern onto a white screen
- Measuring fringe displacement positions for multiple diffraction minima
- Calculating diffraction angles using geometric relationships
- Determining obstacle width for each diffraction order
- Averaging calculated values to obtain the final width estimate

-------------------------------------------------------------------------------------------------------

* Data Structure:

The experimental data is stored in: light_diffraction_data.csv

m = diffraction order minimum

x = fringe displacement from central maximum (in meters)

-------------------------------------------------------------------------------------------------------

* Python Analysis Workflow:

The analysis pipeline automates the diffraction calculations originally performed manually.
Features:

- CSV data import using Pandas
- diffraction angle calculation
- obstacle width determination
- statistical averaging
- uncertainty estimation
- automated plot generation
- processed data export

Libraries Used:

- NumPy
- Pandas
- Matplotlib

-------------------------------------------------------------------------------------------------------

* Interpretation:

The experiment successfully demonstrated the wave behaviour of light through observable diffraction around a microscopic obstacle. The consistency of the calculated widths across multiple diffraction orders supports the validity of both the diffraction model and the measurement methodology.

The newly introduced laboratory laser systems produced sufficiently coherent and stable diffraction patterns for accurate optical analysis and quantitative measurement applications.

-------------------------------------------------------------------------------------------------------

* License:

This project is intended for educational, analytical, and scientific documentation purposes.

