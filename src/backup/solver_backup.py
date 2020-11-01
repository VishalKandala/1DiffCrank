#!/usr/bin/python
import case
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import scheme
import plots
import control

#variable assignment#
Cn1=scheme.Cn1
Cn=scheme.Cn
b=scheme.b

Cin1=scheme.Cin1
bi=scheme.bi

dt=control.dt
vt=control.vt
pt=control.pt
Nt=control.Nt
N=control.N
L=control.L
cfl=control.cfl

plcount=plots.plcount

print('CFL:{:.3}'.format(cfl))

# Initialization #
x=np.linspace(0,L,N) # Grid initialization
u=case.u0(x) #Initial Solution generated.
RHS=Cn.dot(u)+b # Initial RHS value for CN scheme.
RHSi=u+b # Initial RHS value for implicit scheme.


# Figure generation #
#fig = plt.figure()
#ax=plt.axes(projection='3d')
#plt.xlabel('x[m]')
#plt.ylabel('T[K]')
#plt.grid(True)
#plt.title('Evolution of Solution')

# Time series plot Initialization #


# Solution(Time Stepping) #
def Solve(Nt,u,dt,Cin1,RHSi,u,b,Cn1,RHS):
    evol=[]
    start=time.time() # Computational time count started.
    for t in range(Nt):
        if t<=10:
            u=np.linalg.solve(Cin1,RHSi) #Matrix inversion and solution
            RHSi=u+bi #updating RHSi
            RHS=Cn.dot(u)+b #updating RHS
        else:
            u=np.linalg.solve(Cn1,RHS) # Matrix Inversion and solution 
            RHS=Cn.dot(u)+b # Updating RHS based on current iteration u values.

# Plotting T vs x at successive timesteps (every 50 timesteps)
        if (t%vt==0) and (t%pt==0):
       #     plots.vidplot(t,dt,plcount,x,u)
       #    plt.plot(x,u,label='t = {:.3}s'.format(t*dt))
       #    plcount+=1
   #    elif (t%vt==0):
       #    plots.vidplot(t,dt,plcount,x,u)
       #    plcount+=1
   #    elif (t%pt==0):
        #   plt.plot(x,u,label='t = {:.3}s'.format(t*dt)) 
    
        evol.append(np.array([x,u,t*dt]))
    end=time.time()-start
    evol=np.array(evol)
    print("Solution Completed in "+str(end)[:5]+" seconds")
    return evol


#ax.contour3D(evol[0,:]
#plt.plot(x,u,label='t =5.0s', color='k')
#plt.legend()
#plt.savefig('../plots/1dheat.jpg')

#plots.vid()

