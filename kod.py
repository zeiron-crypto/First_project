import matplotlib.pyplot as plt
import numpy as np

plt.plot([0],[0], color='m', marker='o', ms=10)
plt.plot([0],[8], color='m', marker='o', ms=35)
plt.axis('equal')

y0 = 149*10**11
d = 3*y0
alpha = 30
d1 = 5*y0


xt = d*np.sin(alpha*np.pi/180)
yt = d*np.cos(alpha*np.pi/180)
plt.plot([0,xt], [0,yt],'y--')



def f(M=5.9726*10**34,alpha=30):
    r = y0*np.tan(alpha*np.pi/180)
    #M = 5.9726*10**34
    G = 6.67408*10**(-11) 
    C = 3*10**8
    b = (4*G*M)/(r*(C**2))
    u = (90 + alpha)*np.pi/180 - b
    print(b)
    xx = d1*np.cos(u)
    yx = d1*np.sin(u)
    plt.plot([xx,xt], [yx,yt])
    plt.xlim(0,15)
    plt.ylim(0,15)
    plt.axis('equal')
    plt.show()
f()