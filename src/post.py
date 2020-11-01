#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib
import control
import os, sys
import numpy as np

def vid(t,x,evol):    
    matplotlib.rc('font', size=18)
    plcount=0 # picture count for video
    vt=control.vt
    fig=plt.figure()
    fig.set_tight_layout(True);
    for i in range(len(t)):
        if i%vt==0:
            filename='../temp/foo'+str(plcount+1).zfill(3)+'.jpg';
            plt.title('t='+str(t[i])[:3])
            plt.grid(True)
            plt.xlabel('x[m]')
            plt.ylabel('T[K]')
            plt.ylim([0,1])
            plt.plot(x,evol[i]) #label='t='+str(t[i]))
            plt.savefig(filename)
            plt.clf()
            plcount+=1
    os.system("ffmpeg -y -i '../temp/foo%03d.jpg' ../videos/heat_equation.m4v")
    os.system("rm -f ../temp/foo*.jpg")

def evplot(Nt,N,t,x,evol):
    X,T=np.meshgrid(x,t) # Repeats t and x values such that every point in evol has a value in t and x, which is required by contour3D.
    fig = plt.figure()
    plt.grid(True)
    plt.title('Evolution of Solution')
    ax=plt.axes(projection='3d')
    ax.plot_wireframe(evol,X,T,cmap='viridis')
    ax.set_zlabel('t[s]')
    ax.set_ylabel('x[m]')
    ax.set_xlabel('T[K]');
    img='../plots/evol_'+str(Nt).zfill(4)+'_'+str(N).zfill(4)+'.jpg'
    plt.savefig(img)

