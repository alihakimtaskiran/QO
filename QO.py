print("Interacting with reality...")
import numpy as np

class Photon(object):
    def __init__(self,λ,location,direction,spin=(1,0,0),polarization=(1,0)):
        self.__c=299792458#m/s

        self.__location=np.array(location,dtype=np.float32)
        self.__direction=np.array(direction,dtype=np.float32)
        self.__direction=self.__direction/np.linalg.norm(self.__direction)
        if self.__location.shape not in ((),(2,),(3,)):
            raise ValueError("Photons only be allocated in 1D, 2D and 3D")
        if self.__direction.shape not in ((),(2,),(3,)):
            raise ValueError("Photons only be pointed in 1D, 2D and 3D")
        if not self.__direction.shape==self.__location.shape:
            raise ValueError("Position and direction vectors must be in the same dimensions")
        self.__lambdaa=λ

    def evolve_time(self,seconds):
        self.__location+=self.__direction*self.__c*seconds
    
    def info(self):
        return {"wavelenght":self.__lambdaa,"location":self.__location,"direction":self.__direction}
    
class Beam(object):
    def __init__(self,Photons):
        if not type(Photons) in (tuple,list):
            raise TypeError("Photons must be in a tuple or list")
        self.__photons=np.array(Photons)

    def info(self):
        return self.__photons
    
    def evolve_time(self,seconds):
        for i in range(self.__photons.shape[0]):
            self.__photons[i].evolve_time(seconds)
        del i
        
        
class LASER(object):
    def __init__(self,λ,location,direction,intensity):
        if not type(intensity)==int:
            raise TypeError("intensity must be an integer")
        else:
            intensity=int(intensity)
        __x=[]
        for i in range(intensity):
            __x.append(Photon(λ,location,direction))
        self.__beam=Beam(__x)
        del __x,i
    def fire(self):
        return self.__beam
