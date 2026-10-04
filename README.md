
# Modified Palmer–Mansoori Permeability Model
### Fruitland Coal, San Juan Basin

## Project Overview

This project presents a Python-based adaptation of my B.Tech major project on permeability variation in coalbed methane (CBM) reservoirs under pressure depletion.

The original academic work used Excel and MATLAB. For this portfolio version, I recreated the model calculations in Python and organized the input parameters, scenario calculations, and outputs into separate files.

The project focuses on how pressure depletion, matrix shrinkage, and cleat compressibility influence coal permeability.

## Project Objective

To reproduce the Modified Palmer–Mansoori permeability model in Python and examine how permeability changes under different initial porosity and Young’s modulus scenarios.

## Background

Coalbed methane reservoirs contain natural fractures, commonly called cleats, that provide pathways for gas flow.

As reservoir pressure decreases during production, two mechanisms can affect permeability:

- **Matrix shrinkage:** Gas desorption can cause the coal matrix to shrink, potentially increasing cleat aperture.
- **Cleat compressibility:** Changes in effective stress can reduce cleat aperture and permeability.

The model represents the combined influence of these mechanisms on porosity and permeability ratios.

## Model Formulation

The model calculates the normalized porosity ratio:

\[
\frac{\phi}{\phi_i}
=
1+
\frac{(1+\nu)(1-2\nu)}
{(1-\nu)E\phi_i}(p-p_i)
+
\frac{c_0}{\phi_i}
\left(\frac{2(1-2\nu)}{3(1-\nu)}\right)
\left(
\frac{p_i}{p_i+p_L}
-
\frac{p}{p+p_L}
\right)
\]

Permeability ratio is calculated using:

\[
\frac{k}{k_i}=\left(\frac{\phi}{\phi_i}\right)^3
\]

Where:

- \(\phi\) = porosity at pressure \(p\)
- \(\phi_i\) = initial porosity
- \(k\) = permeability at pressure \(p\)
- \(k_i\) = initial permeability
- \(p\) = reservoir pressure
- \(p_i\) = initial reservoir pressure
- \(p_L\) = Langmuir pressure
- \(E\) = Young’s modulus
- \(\nu\) = Poisson’s ratio
- \(c_0\) = cleat compressibility coefficient

## Scenario Analysis

Four scenarios were evaluated using different combinations of initial porosity and Young’s modulus.

| Scenario | Initial Porosity | Young’s Modulus |
|---|---:|---:|
| 1 | 0.001 | 124,000 psi |
| 2 | 0.001 | 445,000 psi |
| 3 | 0.005 | 124,000 psi |
| 4 | 0.005 | 445,000 psi |

The model was evaluated over a pressure range of 0–2,000 psia, at 100-psia intervals.

## Tools and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- CSV files for model and scenario inputs

## Repository Structure

```text
Modified-Palmer-Mansoori-Model/
├── data/
│   ├── model_parameters.csv
│   └── scenario_parameters.csv
├── python/
│   └── Modified_palmer_mansoori_model.py
├── outputs/
│   ├── [generated CSV files]
│   └── [generated PNG plots]
├── Modified_Palmer_Mansoori_Python_Analysis.pdf
├── requirements.txt
└── README.md
```

*The folder and output filenames shown above should match the files included in this repository.*

## Implementation

The Python script reads model parameters and scenario inputs from CSV files, calculates porosity and permeability ratios across the pressure range, and generates output tables and plots.

Pandas is used to read and organize tabular inputs and results. NumPy supports numerical calculations, while Matplotlib is used to visualize the model outputs.

## Key Observations

- The model response varies with initial porosity and Young’s modulus.
- The balance between matrix shrinkage and cleat compressibility influences the calculated permeability response.
- Some extreme-depletion cases produce negative porosity or permeability ratios. These are mathematical outputs of the model formulation and are not physically meaningful permeability values.

## Validation and Limitations

The Python calculations were compared with the original Excel model outputs across the four scenarios.

Small numerical differences may occur because the Python implementation uses the exact value of \(2/3\), while the original Excel model uses the rounded value 0.6667.

The model is reproduced as an analytical calculation and does not include additional physical constraints to prevent nonphysical negative ratios. Results should therefore be interpreted within the limitations of the model.

## Academic Context

This repository is a portfolio adaptation of my B.Tech major project in Applied Petroleum Engineering. The original academic work was developed using Excel and MATLAB; this repository demonstrates my Python-based recreation and analysis of the model.

**Author:** Agamya Jain