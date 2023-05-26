from GWS import UnitGWS
import numpy as np
import matplotlib.pyplot as plt
import argparse

def process_args():
    """
    Process command-line arguments and parse the dictionary of parameters.

    Returns:
    dict: Parsed dictionary of parameters.
    """
    parser = argparse.ArgumentParser(description="Gravitational Wave Source Properties")

    parser.add_argument("-p", type=str, help="Dictionary of parameters")

    args = parser.parse_args()

    params = {}

    if args.p:
        params = dict(item.split("=") for item in args.p.split(","))

    return params

def main():
    params = process_args()

    src = UnitGWS(float(params['d']), float(params['e']), float(params['I']), float(params['i']), float(params['f']))
    power_radiated = src.GWpower()
    h0 = src.optimalStrain()
    hp, hx = src.strain(1)

    print("-dE/dt:", power_radiated)
    print("Optimal, h0:", h0)
    print("h+:", hp)
    print("hx:", hx)
    print("Characteristic Strain, h0:", np.sqrt(hp**2 +hx**2))

if __name__ == "__main__":
    main()