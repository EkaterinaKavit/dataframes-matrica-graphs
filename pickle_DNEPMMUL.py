#work with one PARAMETER:создаем массив значений одного параметра по всем сайтам
#и по всем лотам.

import pandas as pd
import numpy as np

df=pd.read_pickle('F8_32_2.pickle')
df_for_analise=df[df['PARAMETER']=='DNEPMMUL']

#making the dataframe with the meanings for all lots and sites for one PARAMETER
df_site = df_for_analise['6 site']
df_site1 = df_site.append(df_for_analise['15 site'])
df_site2 = df_site1.append(df_for_analise['17 site'])
df_site3 = df_site2.append(df_for_analise['19 site'])
df_site4 = df_site3.append(df_for_analise['28 site'])
#print(df_site4)
# check n/A meanings
#print(df_site4.isnull().sum().sum())

# Take first 6 rows to test transponation, question is open
#df_site_except=df_site.head(6)
#print(df_site_except)

#checking types if df
#print(df_site.dtypes)

#add all information for parameter BNN1014RON
df_for_analise1=df[df['PARAMETER']=='BNN1014RON']
df_site_1 = df_for_analise1['6 site']
df_site1_ = df_site_1.append(df_for_analise1['15 site'])
df_site2_ = df_site1_.append(df_for_analise1['17 site'])
df_site3_ = df_site2_.append(df_for_analise1['19 site'])
df_site4_ = df_site3_.append(df_for_analise1['28 site'])
#print(df_site4_)

result = pd.concat([df_site4,df_site4_],ignore_index=True,names=['index','DNEPMMUL','BNN1014RON'],axis=1)
print(result)

