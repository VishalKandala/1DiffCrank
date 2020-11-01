#!/usr/bin/python

import case 
import numpy as np

#variable assignment #
a=case.a

# Control Parameters # 
N=2000 # Number of grid points.
L=float(1) # Grid Size
Nt=500 # Number of time steps
tf=float(5) # [s] Final time in the simulation.
dt=float(tf/(Nt)) # Time step size.
dx=float(L/(N-1)) # grid spacing
cfl=(a)*dt/((dx)**2) # CFL Number
vt=2 # time step for video plot figures.
pt=100 # time step for overview plot.
plcount=0 # Video image count.


