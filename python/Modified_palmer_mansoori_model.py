import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Define project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

# Load model inputs
model_parameters = pd.read_csv(DATA_DIR / "model_parameters.csv")
scenario_parameters = pd.read_csv(DATA_DIR / "scenario_parameters.csv")

# Extract fixed model parameters
nu = model_parameters.loc[model_parameters["parameter"] == "nu", "value"].iloc[0]
c0 = model_parameters.loc[model_parameters["parameter"] == "c0", "value"].iloc[0]
pi = model_parameters.loc[model_parameters["parameter"] == "pi", "value"].iloc[0]
pL = model_parameters.loc[model_parameters["parameter"] == "pL", "value"].iloc[0]


def palmer_mansoori_model(p, pi, pL, E, nu, phi_i, c0):
    """
    Calculate porosity ratio and permeability ratio
    using the modified Palmer-Mansoori model.
    """

    term1 = (((1 + nu) * (1 - 2 * nu)) / ((1 - nu) * E * phi_i) * (p - pi))
    term2 = ((c0 / phi_i) * (2 * (1 - 2 * nu)) / (3 * (1 - nu)) * ((pi / (pi + pL)) - (p / (p + pL))))

    phi_ratio = 1 + term1 + term2
    k_ratio = phi_ratio ** 3

    return phi_ratio, k_ratio


# Generate pressure values
pressure = np.arange(0, 2001, 100)


# Calculate and save results for each scenario

for _, scenario in scenario_parameters.iterrows():

    E = scenario["E"]
    phi_i = scenario["phi_i"]

    # Call the model function
    phi_ratio, k_ratio = palmer_mansoori_model(
        pressure, pi, pL, E, nu, phi_i, c0
    )

    # Create DataFrame for the current scenario
    scenario_results = pd.DataFrame({
        "Pressure_psia": pressure,
        "phi_ratio": phi_ratio,
        "k_ratio": k_ratio
    })

    # Create scenario-specific filename
    filename = f"results_E{int(E)}_phi{phi_i}.csv"

    # Save scenario results
    scenario_results.to_csv(
        OUTPUTS_DIR / filename,
        index=False
    )

    print(f"Saved: {filename}")


# Generate and save individual plots for each scenario

for _, scenario in scenario_parameters.iterrows():

    E = scenario["E"]
    phi_i = scenario["phi_i"]

    # Create scenario-specific filename
    filename = f"results_E{int(E)}_phi{phi_i}.csv"

    # Read the scenario results
    scenario_results = pd.read_csv(OUTPUTS_DIR / filename)

    # Create plot
    plt.figure(figsize=(8, 6))

    plt.plot(
        scenario_results["Pressure_psia"],
        scenario_results["k_ratio"],
        marker="o"
    )

    plt.xlabel("Pressure (psia)")
    plt.ylabel("Permeability Ratio (k/kᵢ)")

    plt.title(
        "Permeability Ratio vs Pressure\n"
        f"E = {int(E)}, φᵢ = {phi_i}"
    )

    plt.grid(True)

    # Save plot
    plot_filename = f"plot_E{int(E)}_phi{phi_i}.png"

    plt.savefig(
        OUTPUTS_DIR / plot_filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print(f"Saved: {plot_filename}")


# Generate combined comparison plot

plt.figure(figsize=(9, 6))

for _, scenario in scenario_parameters.iterrows():

    E = scenario["E"]
    phi_i = scenario["phi_i"]

    filename = f"results_E{int(E)}_phi{phi_i}.csv"

    scenario_results = pd.read_csv(OUTPUTS_DIR / filename)

    plt.plot(
        scenario_results["Pressure_psia"],
        scenario_results["k_ratio"],
        marker="o",
        label=f"E = {int(E)}, φᵢ = {phi_i}"
    )

plt.xlabel("Pressure (psia)")
plt.ylabel("Permeability Ratio (k/kᵢ)")

plt.title(
    "Modified Palmer–Mansoori Model\n"
    "Permeability Ratio vs Pressure"
)

plt.legend()
plt.grid(True)

plt.savefig(
    OUTPUTS_DIR / "combined_permeability_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("Saved: combined_permeability_plot.png")
