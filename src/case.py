#!/usr/bin/python

import numpy as np

def u0(x):
    a=0.5
    b=0.5
    k1=1
    k2=1
    u=a*np.sin(k1*x)+b*np.cos(k2*x)
    return u

material='Aluminum'
K0= 205 # [W/mK] Thermal conductivity of Rod Material
rho=2710 # [Kg/m**3] Density of Rod Material
cp= 0.91 #[KJ/KgK] Specific Heat of Rod Material
A=1 #[m**2] Cross-section Area of rod
a=K0/(rho*cp) # Diffusion Co-efficient
Q0=0 # Heat flux at left end.
Qn=0 # Heat flux at right end.

