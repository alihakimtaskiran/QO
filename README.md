# QO
Quantum Optic Simulator
<h2>1.1 Tree</h2>
<pre>
|----Photon(object)----|
|                      |---__init__(λ,location,direction,spin=(1,0,0),polarization=(1,0))
|                      |---evolve_time(seconds)
|                      |---info()
|
|
|----Beam(object)------|
|                      |---__init__(Photons)
|                      |---info()
|                      |---evolve_time(seconds)
|
|
|----LASER(object)-----|
                       |---__init__(λ,location,direction,intensity)
                       |---fire()
</pre>
