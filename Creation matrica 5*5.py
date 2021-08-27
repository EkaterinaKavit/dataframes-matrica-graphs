# Создание матрицы вручную и вывод ее на трехмерном графике

import numpy as np
import matplotlib.pyplot as plt

#Создаем двумерную матрицу
A=np.array([[1,1,1,1,1,], [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
#print(A)

#Создаем сетку
fig=plt.figure(figsize=(5,5))
ax_3d=fig.add_subplot(projection="3d")

#Задаем значения, где будет находиться матрица
x=[1,2,3,4,5]
y=[1,3,5,7,9]

xgrid,ygrid=np.meshgrid(x,y)# xgrid - это матрица с х-овой координатой  построчно; ygrid - y-овая координата по столбцам
zgrid= A

print(xgrid)

print(ygrid)
ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()