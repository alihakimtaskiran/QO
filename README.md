# QO
Quantum Optic Simulator
<h2>1.1 Tree</h2>
<pre>
|----Photon(object)----|
|                      |---__init__(λ,location,direction,polarization=(1,0))
|                      |---evolve_time(seconds,n=1,epsilon=8.8541878128e-12)
|                      |---destroy()
|                      |---info()
|
|
|----Beam(object)------|
|                      |---__init__(Photons)
|                      |---info()
|                      |---evolve_time(seconds,n=1,epsilon=8.8541878128e-12)
|
|
|----LASER(object)-----|
                       |---__init__(λ,location,direction,intensity)
                       |---fire()

</pre>
