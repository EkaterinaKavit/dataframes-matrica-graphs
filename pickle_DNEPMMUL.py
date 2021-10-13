#work with one PARAMETER:создаем массив значений одного параметра по всем сайтам
#и по всем лотам.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read pickle
df=pd.read_pickle('F8_32_2.pickle')

#choose unique parameters from the column "PARAMETER" for the loop
#df_without_duplicates=df['PARAMETER'].drop_duplicates()
nd_without_duplicates= df['PARAMETER'].unique()
df_without_duplicates=pd.DataFrame(nd_without_duplicates)
print(df_without_duplicates)

#Create xlsx file with unique
df_without_duplicates.to_excel('unique_parameters1.xlsx')
# df_for_analise=df[df['PARAMETER']=='BNN1010BTA']

for i in df_without_duplicates:
   df_for_analise=df[df['PARAMETER']==i]
   df_site1= df_for_analise['6 site']
   df_site2 = df_site1.append(df_for_analise['17 site'],ignore_index=True)
   df_site3 = df_site2.append(df_for_analise['19 site'],ignore_index=True)
   df_site4 = df_site3.append(df_for_analise['28 site'],ignore_index=True)
   df_site4.to_excel('loop_2_columns.xlsx')


#making the dataframe with the meanings for all lots and sites for one PARAMETER
#df_site = df_for_analise['6 site']
#df_site1 = df_site.append(df_for_analise['15 site'],ignore_index=True)
#df_site2 = df_site1.append(df_for_analise['17 site'],ignore_index=True)
#df_site3 = df_site2.append(df_for_analise['19 site'],ignore_index=True)
#df_site4 = df_site3.append(df_for_analise['28 site'],ignore_index=True)
#print(df_site4)

# check n/A meanings
#print(df_site4.isnull().sum().sum())


#add all information for parameter BNN1014RON
#df_for_analise1=df[df['PARAMETER']=='QBDFIABHCPSA']
#df_site_1 = df_for_analise1['6 site']
# Отладка
#a1=df_site_1.iloc[1:20]
#b1=df_for_analise1['15 site'].iloc[1:20]
#c1=a.append(b, ignore_index=True)
#print(c1)

#df_site1_ = df_site_1.append(df_for_analise1['15 site'],ignore_index=True)
#df_site2_ = df_site1_.append(df_for_analise1['17 site'],ignore_index=True)
#df_site3_ = df_site2_.append(df_for_analise1['19 site'],ignore_index=True)
#df_site4_ = df_site3_.append(df_for_analise1['28 site'],ignore_index=True)
#print (df_site4_)

#result = pd.concat([df_site4,df_site4_],ignore_index=True,axis=1)
#print (type(result))
#result=result.set_axis(['BNN1010BTA','QBDFIABHCPSA'],axis=1,inplace=False)
#print(result)

# Отладка
#result = pd.concat([c,c1],ignore_index=True,names=['index','DNEPMMUL','BNN1014RON'],axis=1)
#print(result)

#graph
#fig = plt.figure(figsize = (7,4))
#ax_3d=fig.add_subplot(projection='3d')

#y=np.linspace(1,10310,10310)
#x=np.linspace(1,2,2)


#xgrid,ygrid=np.meshgrid(x,y)
#zgrid=np.array(result)

#ax_3d.plot_wireframe(xgrid,ygrid,zgrid)
#ax_3d.set_xlabel('x')
#ax_3d.set_ylabel('y')
#ax_3d.set_zlabel('z')
#plt.show()

