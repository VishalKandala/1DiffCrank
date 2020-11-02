import numpy as np
import  argparse
import solver
import post
import scheme
import control
import case

# Argument Parsing #
ap=argparse.ArgumentParser()
ap.add_argument("-s", "--solve", required=True, help='new solution')
ap.add_argument("-u0", "--initial", required=True, help='choose initial function')
arg=vars(ap.parse_args())
flag=int(arg['initial'])
#########################

# Grid Initialization#
Nt=control.Nt
N=control.N
L=control.L
tf=control.tf
x=np.linspace(0,L,N)
t=np.linspace(0,tf,Nt)
########################

# Solve/Reading from previous solution 

if (int(arg['solve'])==1):
#########################
# Pre Processing #

#variable assignment#
    Cn1=scheme.Cn1
    Cn=scheme.Cn
    b=scheme.b
    Cin1=scheme.Cin1
    bi=scheme.bi
    
    cfl=control.cfl
    print('CFL:{:.3}'.format(cfl))

# Initialization #
    if (flag==0):
        u=case.u0(x) #Initial Solution generated.
    elif (flag==1):
        u=case.u1(x) 
    elif (flag==2):
        u=case.u2(x)
    RHS=Cn.dot(u)+b # Initial RHS value for CN scheme.

    RHSi=u+b # Initial RHS value for implicit scheme.
#########################

# Solution #
    soln=solver.solve(N,Nt,u,Cin1,RHSi,bi,Cn,b,Cn1,RHS,flag)
    comptime=soln[1]
    evol=soln[0]
#########################
# Reading Solution from file #
else:
    filename='../results/u_'+str(Nt).zfill(4)+'_'+str(N).zfill(4)+'.csv'
    evol=np.loadtxt(filename,delimiter=',')
    print('solution loaded from file: '+filename)
########################
# Post Processing #

post.snapshots(t,x,evol,flag) 

#post.evplot(Nt,N,t,x,evol,flag) # Plot Time evolution surface.

#post.vid(t,x,evol) # Create Function evolution video.   

