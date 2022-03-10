from QO import *
import matplotlib.pyplot as plt
Continumm=Field(3)          
S_1=Shiny((0,0,1),(0,1),1,5.45e+14)
S_2=Shiny((0,2,2),(0,1),1,5.45e+14)

Continumm.add((S_1,S_2))

observers=[]
pix=1e-6
for i in range(-250,250):
    for j in range(-250,250):
        observers.append((i*pix,j*pix,0))
        
im=np.array(Continumm.observe(observers,.5))
plt.imshow(im.reshape((500,500)),cmap="Greens")
