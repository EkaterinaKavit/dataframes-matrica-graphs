
# Вывод функции на трехмерном графике
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#Создаем одномерные массивы вручную
#x=[1,2,3]
#y=[2,5,6,8]

# Создаем сетку(ее можно создать двумя способами:
# 1 способ: #from mpl_toolkits.mplot3d import Axes3D, тогда #ax_3d=Axes3D(fig)
#2 способ; fig = plt.figure(figsize = (7,4)), ax_3d=fig.add_subplot(projection='3d') в этом способе mplot не нужен


fig = plt.figure(figsize = (7,4))
#ax_3d=Axes3D(fig)
ax_3d=fig.add_subplot(projection='3d')

# Создаем одномерный массив со значениями от 0 до 10, 50 значений и задаем функцию
#x=np.linspace(0,10,50)
#z=np.cos(x)


x=np.arange(-2*np.pi,2*np.pi,0.2)
y=np.arange(-2*np.pi,2*np.pi,0.2)

# Создаем две двумерные матрицы для создания сетки функции(xgrid - матрица с х-выми координатами)
xgrid,ygrid=np.meshgrid(x,y)

zgrid=np.sin(xgrid)*np.sin(ygrid)/(xgrid*ygrid)

ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
plt.show()