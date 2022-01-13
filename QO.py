print("Interacting with reality...")
import os

class PhotonField(object):
    def __init__(self,dim):
        self.__dim=dim
        self.__Φ=""
        self.c=299792458#m/s
    
    def shine(self,location,presence,amplitude, frequency, phase=0):
        if not(type(location)==tuple or type(location)==list):
            raise TypeError("Location of the light must be a list or tuple")
        location=tuple(location)
        if not( type(presence)==tuple or type(presence)==list):
            raise TypeError("Presence of the light must be a list or tuple")
        if not type(amplitude)==float:
            raise TypeError("Amplitude of the light must be real scalar")
        if not( type(frequency)==float or type(frequency)==int):
            raise TypeError("Frequency of the light must be real scalar")
        if not( type(phase)==float or type(phase)==int):
            raise TypeError("phase of the light must be real scalar")
        d=len(location)
        if not d==self.__dim:
            raise ValueError("Location must have the same dimensions with the entity")
        for i in range(d):
            self.__Φ+=str(location[i])+","
        self.__Φ+=str(presence[0])+","
        self.__Φ+=str(presence[1])+","
        self.__Φ+=str(amplitude)+","
        self.__Φ+=str(frequency)+","
        self.__Φ+=str(phase)+"\n"
        
     
       
    def observeC(self,location,moment):
        if not(type(location)==tuple or type(location)==list):
            raise TypeError("Location of the light must be a list or tuple")
        if not (type(moment)==float or type(moment)==int):
            raise TypeError("the moment is a scalar")
        r_val=0
        file=open("result.cw","w")
        file.write("")
        file.close()
        file=open("wave.cw","w")
        file.write(self.__Φ)
        file.close()
        file=open("observer.cw","w")
        _=""
        _+=str(moment)
        _+=","+str(moment)
        for i in range(self.__dim):
            _+=","+str(location[i])
        
        
        file.write(_)
        file.close()
        os.system("./renderer.bin")
        file=open("result.cw")
        r_val=float(file.read())
        file.close()
        return r_val   
