print("Interacting with reality...")
import numpy as np

class Photon(object):
    def __init__(self,λ,location,direction):
        self.c=299792458#m/s

        self.location=np.array(location,dtype=np.float32)
        self.direction=np.array(direction,dtype=np.float32)
        if self.location.shape not in ((),(2,),(3,)):
            raise ValueError("Photons only be allocated in 1D, 2D and 3D")
        if self.direction.shape not in ((),(2,),(3,)):
            raise ValueError("Photons only be pointed in 1D, 2D and 3D")
        self.lambdaa=λ

    def evolve_time(self,seconds):
        co=self.c/np.linalg.norm(self.direction)
        self.location+=self.direction*co*seconds
    
    def get_location(self):
        return self.location
    
    def get_direction(self):
        return self.location
        
    def get_wavelenght(self):
        return self.lambdaa
