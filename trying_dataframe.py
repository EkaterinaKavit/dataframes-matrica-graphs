#Считывание информации из эксель и печать необходимого куска

import pandas as pd

df=pd.read_excel('first_try_excel.xlsx', engine='openpyxl')

#df1=df.iloc[3:5,2:5]
#df1.to_excel('statistics1.xlsx')
#df['PARAMETER']
#df[['Lot','WAFER']]
