import sys
import configparser
import numpy as np
import matplotlib.pyplot as plt
from GWS import UnitGWS

def read_config_file(filename):
    """
    Read the properties from a config file.

    Args:
    filename (str): Name of the config file.

    Returns:
    dict: Dictionary of properties.
    """
    config = configparser.ConfigParser()
    config.read(filename)

    properties = {}
    for section in config.sections():
        properties[section] = {
            'd': float(config.get(section, 'distance')),
            'e': float(config.get(section, 'ellipticity')),
            'I': float(config.get(section, 'moment')),
            'i': float(config.get(section, 'inclination')),
            'f': float(config.get(section, 'frequency')),
            'ra': float(config.get(section, 'RA')),
            'de': float(config.get(section, 'declination')),
        }

    return properties

def characteristics(properties):
    fGW = []
    strain = []
    rad = []

    for obj in properties.values():
        fGW.append(obj['f'])
        src = UnitGWS(obj['d'], obj['e'], obj['I'], obj['i'], obj['f'])
        power_radiated = src.GWpower()
        h0 = src.optimalStrain()
        hp, hx = src.strain(1)
        h_sd = src.spindownStrain(1)
        strain.append(np.sqrt(hp**2 + hx**2))
        rad.append(power_radiated)
    
    return fGW, strain, rad

def main():
    if len(sys.argv) < 2:
        print("Please provide the config file as an argument.")
        return

    filename = sys.argv[1]
    properties = read_config_file(filename)
    fGW, strain, rad = characteristics(properties)

    fig, (ax1, ax2) = plt.subplots(2)
    
    ax1.scatter(fGW, strain)
    ax2.scatter(fGW, rad)
    ax1.set_ylabel('Characteristics Strain')
    ax2.set_ylabel('Power Radiated')
    ax2.set_xlabel('frequency')
    plt.show()

if __name__ == '__main__':
    main()