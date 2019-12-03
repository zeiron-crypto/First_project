import matplotlib.pyplot as plt
import numpy as np

plt.plot([0],[0], color='g', marker='o', ms=15, label ='планета1')
plt.plot([0],[2.8*10**12], color='k', marker='o', ms=25,label ='планета2')
plt.plot([-3*10**12],[5*10**12], color='y', marker='o', ms=8,label ='звезда')
plt.plot([3.5*10**12],[6.2*10**12], color='y', marker='o', ms=8,label ='мнимая звезда')

plt.axis('equal')

y0 = 142*10**10
d = 2.5*y0
alpha = 30
d1 = 4*y0



xt = d*np.sin(alpha*np.pi/180)
yt = d*np.cos(alpha*np.pi/180)
plt.plot([0,xt], [0,yt],'c--')

d3 = 5*y0

xtt = d3*np.sin(alpha*np.pi/180)
ytt = d3*np.cos(alpha*np.pi/180)
plt.plot([0,xtt], [0,ytt],'c--',label ='искривлённый луч')


def f(M=5.9726*10**34,alpha=30):
    r = y0*np.tan(alpha*np.pi/180)
    #M = 5.9726*10**34
    G = 6.67408*10**(-11) 
    C = 3*10**8
    b = (4*G*M)/(r*(C**2))
    u = (90 + alpha)*np.pi/180 - b
    #print(b)
    xx = d1*np.cos(u)
    yx = d1*np.sin(u)
    plt.plot([xx,xt], [yx,yt],label ='луч')
    plt.xlim(0,15)
    plt.ylim(0,15)
    plt.axis('equal')
    plt.legend()
    plt.show()
f()
