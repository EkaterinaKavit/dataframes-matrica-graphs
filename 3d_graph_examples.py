import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (7,4))

ax_3d=fig.add_subplot(projection='3d')

x=[2,4,6]
y=[1,2,3]

xgrid,ygrid=np.meshgrid(x,y)
zgrid=2*xgrid*ygrid/(xgrid+ygrid)

print(zgrid)

ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

zgrid=3*xgrid*ygrid/(xgrid+ygrid)
ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

zgrid=xgrid*ygrid/(xgrid+ygrid+1)
ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()
