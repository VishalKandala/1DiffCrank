#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib
import control
import os, sys
import numpy as np
import math as m

def vid(t,x,evol,flag):    
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
    os.system("ffmpeg -y -i '../temp/foo%03d.jpg' ../videos/heat_equation_"+str(flag)+".m4v")
    os.system("rm -f ../temp/foo*.jpg")

def snapshots(t,x,evol,flag):
    matplotlib.rc('font',size=12)
    pt=control.pt
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    axs[0, 0].plot(x,evol[0])
    axs[0,0].set_title('t='+str(t[0])[:3])
    axs[0,0].set_ylabel('T[K]')
    #axs[0,0].set_xlabel('x[m]')
    axs[0,1].plot(x,evol[pt])
    axs[0,1].set_title('t='+str(t[pt])[:3])
    axs[0,1].set_ylabel('T[K]')
    #axs[0,1].set_xlabel('x[m]')
    axs[1,0].plot(x,evol[m.ceil(2.5*pt)])
    axs[1,0].set_title('t='+str(t[m.ceil(2.5*pt)])[:3])
    axs[1,0].set_ylabel('T[K]')
    axs[1,0].set_xlabel('x[m]')
    axs[1,1].plot(x,evol[-1])
    axs[1,1].set_title('t='+str(t[-1])[:3])
    axs[1,1].set_ylabel('T[K]')
    axs[1,1].set_xlabel('x[m]')
    img='../plots/snap_'+str(flag)+'_'+str(len(t)).zfill(4)+'_'+str(len(x)).zfill(4)+'.jpg'
    plt.savefig(img)

def evplot(Nt,N,t,x,evol,flag):
    X,T=np.meshgrid(x,t) # Repeats t and x values such that every point in evol has a value in t and x, which is required by contour3D.
    fig = plt.figure()
    plt.grid(True)
    plt.title('Evolution of Solution')
    ax=plt.axes(projection='3d')
    ax.plot_surface(T,X,evol,cmap='viridis')
    ax.set_zlim([0,1])
    ax.set_xlabel('t[s]')
    ax.set_ylabel('x[m]')
    ax.set_zlabel('T[K]');
    #ax.invert_yaxis()
    img='../plots/evol'+str(flag)+'_'+str(Nt).zfill(4)+'_'+str(N).zfill(4)+'.jpg'
    plt.savefig(img)

