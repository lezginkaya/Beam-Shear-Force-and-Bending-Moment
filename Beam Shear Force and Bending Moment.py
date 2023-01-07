import numpy as np
import matplotlib.pyplot as plt

w= 1500 #N/m
l=1 #length of the beam (m)

def shear_force(x):
    return w*((l/2)-x)

distance=np.arange(0,1,0.01)
v=shear_force(distance)

def bending_moment(x):
    return (w*x/2)*(l-x)

m=bending_moment(distance)
fig=plt.figure(figsize=(7,8))
ax1=fig.add_subplot(2,1,1)
ax1.fill_between(distance,v,color="green", alpha=0.5, hatch="||")
ax1.set_xlim(0,1)
ax1.set_ylim(-900,900)
ax1.set_title("Shear Force")
ax1.set_ylabel("Shear Force(N)")
ax1.plot(distance,v)

ax2=fig.add_subplot(2,1,2)
ax2.plot(distance,m)
ax2.fill_between(distance,m,color="red", alpha=0.5, hatch="||")
ax2.set_ylim(0,250)
ax2.set_title("Bending Moment")
ax2.set_ylabel("Bending Moment(Nm)")
ax2.set_xlim(0,1)
plt.show()