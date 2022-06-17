# QO
## Wave Optic Simulator
Light... The most exciting part of the existance... We have various models to explain the behavior of the light. One of them is Wave Optics. Wave Optics emerges, as the ray optic couldn't explain the phenomenons of interference and diffraction. Wave optic, understood by the name, explains the light as wave. Phase of the wave varies throug the time and location of the field. The QO simulates this behaviours. You can locate arbitrary light sources in the space and observe them from wherever you want. The QO has accelerated renderer. It has easy to learn python API and C++ backend. You only program easily with python and C++ handles the heavy computations.

<h2>1.1 Tree</h2>
<pre>
|----PhotonField(object)----|
|                           |--- __init__(dim)
|                           |---add(content)
|                           |---observe(locations, moment)
|
|----Shiny(object)----------|
                            |---__init__(location, presence, amplitude, frequency, phase=0)

</pre>
<h2>How to Install</h2>
Download <a href="https://raw.githubusercontent.com/alihakimtaskiran/QO/main/QO.py" target="_blank">QO.py</a> and <a href="https://github.com/alihakimtaskiran/QO/raw/main/render.cpp" target="_blank">renderer.cpp</a>. Then compile the c++ file named as **renderer.bin**. After that add the binary file into the same directory with **QO.py**. It's ready to work.
