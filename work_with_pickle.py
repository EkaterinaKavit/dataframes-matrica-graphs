import pandas as pd
import matplotlib.pyplot as plt

wish_parameters = ['BNN1010BTA','BNN1010BV']
#df=pd.read_excel('F8_PT_32kp_2.xlsx', engine='openpyxl')
#df.to_pickle('F8_32_2.pickle')
df1=pd.read_pickle('F8_32_2.pickle')
#print(df1.head(15))
#print(df1['6 site'].head(15))

#print(wish_parameters[1])
df1[(df1['LOT']=='M433015_FIN')&(df1['PARAMETER']=='BNN1010BTA')].pivot_table(values='6 site', index='WAFER', fill_value=None,margins=False,dropna=True).plot(kind='line')
