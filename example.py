import QO
a=QO.PhotonField(2) #Create a 2D field
for i in range(1000):
    a.shine((5.6,78.6),(0,4),3.5,5.694848383,i) #Add light sources with various phases

b=a.observeC((0,1), 2) #observe the light
