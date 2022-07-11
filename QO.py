print("Interacting with reality...")
import os
import numpy as np
try:
    os.system("mkdir MemoriesWillNeverFade") #For the memory of survey of learning photonics. Appreciate all inspiring me
except:
    pass

class PhotonField(object):
    def __init__(self,dim):
        if not type(dim)==int:
            raise TypeError("Number of dimensions is an integer")
        if dim<1:
            raise ValueError("Number of dimensions must be more than 1")
        self.__dim=dim
        self.__shinies=[]
        
    def add(self, content):
        if not type(content) in {list, tuple}:
            content = (content,)
        
        for sub_content in content:
            if type(sub_content)==Shiny:
                _=len(sub_content.info[0])
                if not _==self.__dim:
                    raise ValueError(f"The source must be located in {self.__dim}-D space. But, it is located in {_}-D space")
                self.__shinies.append(sub_content)

    def observe(self, locations, moment):
        locations=np.array(locations)
        if not locations.shape==(self.__dim,):
            if not locations.shape[1]==self.__dim:
                raise ValueError("Observer's locations must be N×D array. N is number of observers D is dimensions of the entity")
                
        else:
            locations=np.array((locations,))
            
        np.savetxt("MemoriesWillNeverFade/observers.wm",locations , delimiter=",")  
        files=(open("MemoriesWillNeverFade/meta.wm","w"),open("MemoriesWillNeverFade/locations.wm","w"),open("MemoriesWillNeverFade/amplitudes.wm","w"),open("MemoriesWillNeverFade/frequencies.wm","w"),open("MemoriesWillNeverFade/phases.wm","w"),open("MemoriesWillNeverFade/result.wm","w"))
        files[0].write(str(self.__dim)+"\n"+str(len(self.__shinies))+"\n"+str(moment)+"\n"+str(locations.shape[0]))
        for glimmer in self.__shinies:
            if glimmer.info[1][0]<=moment<=glimmer.info[1][1]:
                files[1].write(str(glimmer.info[0])[1:-1]+"\n")
                files[2].write(str(glimmer.info[2])+"\n")
                files[3].write(str(glimmer.info[3])+"\n")
                files[4].write(str(glimmer.info[4])+"\n")
        
        for file in files:
            file.close()
        
        os.system("./renderer.bin")
        return np.genfromtxt("MemoriesWillNeverFade/result.wm",delimiter=";")
        
            


class Shiny(object):
    def __init__(self, location, presence, amplitude, frequency, phase=0):
        if type(location) not in {list, tuple}:
            raise TypeError("Location must be a list or tuple")

        if type(presence) not in {list, tuple}:
            raise TypeError("Presence must be a list or tuple")

        if type(amplitude) not in {int, float}:
            raise TypeError("Amplitude must be a int or float")       

        if type(frequency) not in {int, float}:
            raise TypeError("Frequency must be a int or float")

        if type(phase) not in {int, float}:
            raise TypeError("Phase must be a int or float")

        self.info=(location, presence, amplitude, frequency, phase)
