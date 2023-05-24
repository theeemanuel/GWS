import numpy as np

# Constants
G = 6.67430e-11   # Gravitational constant in m^3 kg^−1 s^−2
c = 2.99792458e8  # Speed of light in m/s
a = ( 4*np.pi**2*G/c**4 ) * 1e-6 * 1e38 * 1e6 * ( 1/3.08e19 )

# Dummy Gravitational Wave Source (GWS) parent class
class GWS:
    def __init__(self, *props):     #injection properties *props = (distance)
        self.distance = props[0]

    def GWpower(self):
        pass

    def optimalStrain(self):
        pass

    def strain(self):
        pass

# Derived class for single rotation sources
class UnitGWS(GWS):
    def __init__(self, *props):     #injection properties *props = (distance, ellipcity, inertialMoment, inclination, frequency)
        super().__init__(props[0])
        self.ellipticity = props[1]
        self.inertialMoment = props[2]
        self.inclination = props[3]
        self.frequency = props[4]

    def GWpower(self):
        return (1.7e33)*(self.inertialMoment**2)*(self.ellipticity**2)*(self.frequency**6)

    def optimalStrain(self):
        return ( a*self.ellipticity*self.inertialMoment*(self.frequency**2)/self.distance )
    
    def strain(self, t):
        inclination_rad = np.radians(self.inclination)

        h0 = ( a*self.ellipticity*self.inertialMoment*(self.frequency**2)/self.distance )

        hp = ( h0 * 0.5*(1 + np.cos(self.inclination)**2) * np.cos(2*np.pi*self.frequency*t) )
        hx = ( h0 * np.cos(self.inclination) * np.sin(2*np.pi*self.frequency*t) )

        return hp, hx