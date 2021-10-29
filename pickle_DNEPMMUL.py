import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import sklearn
from sklearn import preprocessing as per
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer


df=pd.read_pickle('F8_32_2.pickle')

nd_without_duplicates= df['PARAMETER'].unique()
df_without_duplicates=pd.DataFrame(nd_without_duplicates)

#df_without_duplicates.to_excel('unique_parameters1.xlsx')

result=pd.DataFrame()

for i in df_without_duplicates[0]:

   df_for_analise=df[df['PARAMETER']==i]
   df_site1= df_for_analise['6 site']
   df_site2 = df_site1.append(df_for_analise['17 site'],ignore_index=True)
   df_site3 = df_site2.append(df_for_analise['19 site'],ignore_index=True)
   df_site4 = df_site3.append(df_for_analise['28 site'],ignore_index=True)
   result= pd.concat([result,df_site4],ignore_index=True,axis=1)






fig = plt.figure(figsize = (40,20))
ax_3d=fig.add_subplot(projection='3d')

y=np.linspace(1,8248,8248)# y- количество строк
x=np.linspace(1,452,452) # x - количество столбцов


xgrid,ygrid=np.meshgrid(x,y)
zgrid=np.array(result)

for i, row in enumerate(zgrid):
   for j, num in enumerate(row):
      if num>500: zgrid[i][j]=0;
      if num<-1000: zgrid[i][j]=0;
#Rescaling
scaler=per.MinMaxScaler(feature_range=(0,1))
rescalezgrid=scaler.fit_transform(zgrid)

#Standartization

scaler=StandardScaler().fit(zgrid)
standardizedzgrid=scaler.transform(zgrid)

#print(standardizedzgrid)

#Normalization
#scaler=Normalizer().fit(zgrid)
#normalizezgrid=scaler.transform(zgrid)
#print(normalizezgrid)


surf=ax_3d.plot_surface(xgrid,ygrid,standardizedzgrid,cmap=cm.hsv)
ax_3d.plot_wireframe(xgrid,ygrid,standardizedzgrid)
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

#fig.colorbar(surf)#, shrink=0.5, aspect=5)

plt.show()

