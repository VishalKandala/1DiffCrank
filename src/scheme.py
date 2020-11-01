#!/usr/bin/python
import control
import case
import numpy as np

# variable assignment #
cfl=control.cfl
N=control.N
dx=control.dx

Q0=case.Q0
Qn=case.Qn
##############################
# Crank Nicholson Scheme #

# Co-efficient Matrix Initialization #
Cn1=np.zeros((N,N)) # Co-efficient matrix of (n+1)th U vector.
Cn=np.zeros((N,N)) # Co-efficient matrix of (nth)th U vector.
b=np.zeros((N)) # Boundary Conditions vector.

# Co-efficient Matrix Population #
# Interior Lattice #
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


# Neumann Boundary conditions #

# Main Diagonal terms #
Cn1[0,0]=1+cfl
Cn[0,0]=1-cfl
Cn1[-1,-1]=1+cfl
Cn[-1,-1]=1-cfl

# Upper and Lower Diagonals
Cn1[0,1]=-cfl # Neumann BC u0_x=Const.
Cn[0,1]=cfl   # Neumann BC u0_x=Const.
Cn1[-1,-2]=-cfl # Neumann BC un_x=Const.
Cn[-1,-2]=cfl # Neumann BC un_x=Const.

#Boundary Flux vector #
b[0]=2*cfl*dx*Q0 # Heat Flux at x=0
b[-1]=2*cfl*dx*Qn # Heat Flux at x=L
##################################
# Backward Euler Scheme #

# Co-efficient Matrix Initialization #
Cin1=np.zeros((N,N)) # Co-efficient matrix of (n+1)th U vector.
bi=np.zeros((N)) # Boundary Conditions vector.

# Co-efficient Matrix Population #

# Interior Lattice #
for i in range(1,N-1):
    for j in range(1,N-1):
        if j==i: # Main Diagonal terms
            Cin1[i,j]=1+2*cfl
        elif j==(i-1): # Diagonal below the main Diagonal
            Cin1[i,j]= -cfl
        elif j==(i+1): # Diagonal above the main Diagonal
            Cin1[i,j]= -cfl 
        else:
            Cin1[i,j]=0

# Neumann Boundary conditions #
# Main Diagonal terms #
Cin1[0,0]=1+2*cfl
Cin1[-1,-1]=1+2*cfl                                                                                                                                                                      

# Upper and Lower Diagonals
Cin1[0,1]=-2*cfl # Neumann BC u0_x=Const.
Cin1[-1,-2]=-2*cfl # Neumann BC un_x=Const.

#Boundary Flux vector #
bi[0]=cfl*dx*Q0 # Heat Flux at x=0
bi[-1]=cfl*dx*Qn # Heat Flux at x=L


