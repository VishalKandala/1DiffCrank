#!/usr/bin/python
import time
import numpy as np
# Solution(Time Stepping) #

def solve(N,Nt,u,Cin1,RHSi,bi,Cn,b,Cn1,RHS):
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
        evol.append(u)
    end=time.time()-start
    evol=np.array(evol)
    filename='../results/u_'+str(Nt).zfill(4)+'_'+str(N).zfill(4)+'.csv'
    np.savetxt(filename,evol,delimiter=',')
    print("Solution Completed in "+str(end)[:5]+" seconds")
    return evol
