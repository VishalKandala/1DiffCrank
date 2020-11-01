#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import time
import os, sys
import matplotlib


# Crank Nicholson Scheme 
# 1D Heat Equation

def init1(x):
    u=np.sin(x)+0.5*np.cos(x)
    return u

# Solver Parameters #
N=1000 # Number of grid points.
L=float(1) # Grid Size
Nt=2500 # Number of time steps
tf=float(5) # [s] Final time in the simulation.
dt=float(tf/(Nt)) # Time step size.
dx=float(L/(N-1)) # grid spacing

# Case Parameters #
material='Aluminum'
K0= 205 # [W/mK] Thermal conductivity of Rod Material
rho=2710 # [Kg/m**3] Density of Rod Material
cp= 0.91 #[KJ/KgK] Specific Heat of Rod Material
A=1 #[m**2] Cross-section Area of rod
a=K0/(rho*cp) # Diffusion Co-efficient
cfl=a*dt/(dx)**2 # Cfl Number
Q0=0 # Heat flux at left end.
Qn=0 # Heat flux at right end.

print(cfl)

# Co-efficient Matrix Initialization #
Cn1=np.zeros((N,N)) # Co-efficient matrix of (n+1)th U vector.
Cn=np.zeros((N,N)) # Co-efficient matrix of (nth)th U vector.
b=np.zeros((N)) # Boundary Conditions vector.

# Co-efficient Matrix Population #

for i in range(1,N-1):
    for j in range(1,N-1):
        if j==i: # Main Diagonal terms
            Cn1[i,j]=1+cfl
            Cn[i,j]=1-cfl
        elif j==(i-1): # Diagonal below the main Diagonal
            Cn1[i,j]= -cfl/2
            Cn[i,j]=cfl/2
        elif j==(i+1): # Diagonal above the main Diagonal
            Cn1[i,j]= -cfl/2
            Cn[i,j]=cfl/2  
        else:
            Cn[i,j]=0
            Cn1[i,j]=0

# Boundary conditions #
Cn1[0,0]=1+cfl
Cn[0,0]=1-cfl
Cn1[-1,-1]=1+cfl
Cn[-1,-1]=1-cfl
Cn1[0,1]=-cfl # Neumann BC u0_x=Const.
Cn[0,1]=cfl   # Neumann BC u0_x=Const.
Cn1[-1,-2]=-cfl # Neumann BC un_x=Const.
Cn[-1,-2]=cfl # Neumann BC un_x=Const.
b[0]=2*cfl*dx*Q0 # Heat Flux at x=0
b[-1]=2*cfl*dx*Qn # Heat Flux at x=L

#print(b)
#print(Cn1)


# Solution Initialization #
x=np.linspace(0,L,N)
#u=np.asarray([2*xx if xx <= 0.5 else 2*(1-xx) for xx in x]) # Parabolic Initial solution.
u=init1(x)
RHS=Cn.dot(u)+b # Initial RHS
#print(RHS)
# Plot Parameters #
matplotlib.rc('font', size=18)
#matplotlib.rc('font', family='Arial')
fig=plt.figure()
plcount=0 # Plot counter
nplot=50 # Number of successive timesteps after which to plot results
fig.set_tight_layout(True);


start=time.time()

# Solution(Time Stepping) #
for t in range(Nt):
    u=np.linalg.solve(Cn1,RHS) # Matrix Inversion and solution 
    RHS=Cn.dot(u)+b # Updating RHS based on current iteration u values.
    
# Plotting T vs x at successive timesteps (every 50 timesteps)   
    if (t%nplot==0):
        filename='foo'+str(plcount+1).zfill(3)+'.jpg';
        plt.title('t='+str(t*dt)[:3])
        plt.grid(True)
        plt.xlabel('x[m]')
        plt.ylabel('T[K]')
        plt.ylim([0,1])
        plt.plot(x,u) #label='t='+str(t))
        plt.savefig(filename)
        plt.clf()
        plcount+=1
end=time.time()-start

print("Solution Completed in "+str(end)+" seconds")

os.system("ffmpeg -y -i 'foo%03d.jpg' heat_equation.m4v")
os.system("rm -f *.jpg")

