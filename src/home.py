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
arg=vars(ap.parse_args())
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
    u=case.u0(x) #Initial Solution generated.

    RHS=Cn.dot(u)+b # Initial RHS value for CN scheme.

    RHSi=u+b # Initial RHS value for implicit scheme.
#########################

# Solution #
    evol=solver.solve(N,Nt,u,Cin1,RHSi,bi,Cn,b,Cn1,RHS)
#########################
# Reading Solution from file #
else:
    filename='../results/u_'+str(Nt).zfill(4)+'_'+str(N).zfill(4)+'.csv'
    evol=np.loadtxt(filename,delimiter=',')
    print('solution loaded from file: '+filename)
########################
# Post Processing #

post.evplot(Nt,N,t,x,evol) # Plot Time evolution surface.

post.vid(t,x,evol) # Create Function evolution video.   

