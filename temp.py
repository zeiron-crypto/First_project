import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import ArtistAnimation
#fig = plt.figure()



x = np.arange(5,6.3,0.1)
y = 1*(x-4.4)**2+1*(x-4.4)+4
plt.plot(x,y,'b')


plt.plot([5.3,9], [11.8,1],'b')

plt.plot([3.8,8.6], [2.8,11.8],'y--')

circle1 = plt.Circle((3,8), 2, color='m', fill=False)


ax=plt.gca()
ax.add_patch(circle1)
plt.axis('scaled')


circle2 = plt.Circle((3,2), 1, color='c', fill=False)

ax=plt.gca()
ax.add_patch(circle2)
plt.axis('scaled')

plt.plot([4,4.7,5,5.2,5.8,5.3,5,4.6,4], [12,12.5,13,12.5,12,11.8,11.3,11.9,12])

plt.plot([8,8.7,9,9.2,9.8,9.3,9,8.6,8], [12,12.5,13,12.5,12,11.8,11.3,11.9,12],'--')


plt.xlim(0,15)
plt.ylim(0,15)
plt.show()
  
