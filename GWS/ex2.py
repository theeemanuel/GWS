from GWS import UnitGWS
import numpy as np
import argparse

def process_args():
    """
    Process command-line arguments.

    Returns:
    argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Gravitational Wave Source Properties")

    parser.add_argument("-d", "--distance", type=float, help="Distance to the source in kpc")
    parser.add_argument("-e", "--ellipticity", type=float, help="Equatorial ellipticity in (e/10^-6) units")
    parser.add_argument("-I", "--moment_of_inertia", type=float, help="I_{zz} in (I_{zz}/I0) units")
    parser.add_argument("-i", "--inclination", type=float, help="Inclination angle of the source in degrees")
    parser.add_argument("-f", "--frequency", type=float, help="Frequency in kHz")
    parser.add_argument("-s", "--frequency shift rate", type=float, help="Frequency shift rate in 10^-10 Hz/s")

    args = parser.parse_args()
    return args

def main():
    args = process_args()

    d = args.distance
    e = args.ellipticity
    I = args.moment_of_inertia
    i = args.inclination
    f = args.frequency

    src = UnitGWS(d, e, I, i, f)
    power_radiated = src.GWpower()
    h0 = src.optimalStrain()
    hp, hx = src.strain(1)
    h_sd = src.spindownStrain(1)

    print("-dE/dt: ", power_radiated)
    print("Optimal, h0: ", h0)
    print("h+: ", hp)
    print("hx: ", hx)
    print("Characteristic Strain, h0: ", np.sqrt(hp**2 +hx**2))
    print("h_spindown: ", h_sd)

if __name__ == "__main__":
    main()