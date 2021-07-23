# Calculation the correlation between sinus and cosinus
import math
import pandas as pd
import pylab as plt

# Создаем пустой список и добавляем туда значения синусов
a=[]
for i in range(20):
    a.append(math.sin(i))
print (a)
# Создаем пустой список и добавляем туда значения косинусов
b=[]
for i in range(20):
    b.append(math.cos(i))
print (b)
#Использование Series для преобразования списка в новые обрабатываемые данные pandas
astd=pd.Series(a)
bstd=pd.Series(b)
# Вычислить стандартное отклонение, при округлении (a, 4) сохраняются первые четыре десятичных разряда
a_b_std=round(astd.corr(bstd),4)
print("Корреляция между синусом и косинусом",a_b_std)

# Рисуем диаграмму
plt.scatter(a,b)
plt.title('Корреляция:' + str(a_b_std), fontproperties='SimHei')
plt.show()