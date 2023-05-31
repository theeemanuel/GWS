import random
import configparser
import numpy as np

def generate_objects(num_objects):
    """
    Generate a specified number of objects with random properties.

    Args:
    num_objects (int): Number of objects to generate.

    Returns:
    list: List of objects with properties.
    """
    objects = []
    for i in range(1, num_objects+1):
        obj = {}
        obj['name'] = f'Object{i}'
        obj['distance'] = random.uniform(1, 10)
        obj['ellipticity'] = random.uniform(1.0, 2.0)
        obj['moment'] = random.uniform(1.0, 2.0)
        obj['inclination'] = random.uniform(0, 2*np.pi)
        obj['frequency'] = random.uniform(0.1, 1.5)
        obj['RA'] = random.uniform(0, 2*np.pi)
        obj['declination'] = random.uniform(-np.pi/2, np.pi/2)
        objects.append(obj)
    return objects

def write_config_file(objects, filename):
    """
    Write the objects' properties to a config file.

    Args:
    objects (list): List of objects with properties.
    filename (str): Name of the config file to write.
    """
    config = configparser.ConfigParser()
    for obj in objects:
        section_name = obj['name']
        config[section_name] = obj
    with open(filename, 'w') as configfile:
        config.write(configfile)

def main():
    num_objects = 500
    objects = generate_objects(num_objects)
    write_config_file(objects, 'config.ini')

if __name__ == '__main__':
    main()