import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wish_parameters = ['BNN1', 'BNN2']
#wish_parameters = ['EN1', 'EN2']

# сравнить пв на участках корреляции параметров и малой дисперсии  и   на участках рассинхрона параметров и большой дисперс 
#wish_parameters = ['EN12', 'EN13', 'EN14', 'EN15']


#df=pd.read_excel('F.xlsx', engine='openpyxl')
#df.to_pickle('F.pickle')
df1 = pd.read_pickle('F.pickle')

for i in wish_parameters:
#for i in set(df1['PARAMETER'].tolist()):
    df_for_plotting = df1[df1['PARAMETER'] == i]
    #df_for_plotting = df_for_plotting[300:700]

    #df_for_plotting = df1[df1['PARAMETER'] == 'DNL']
    #df_wish_param = df_for_plotting[(df_for_plotting['6 site']<150) & (df_for_plotting['6 site']>-30)]
    #df_wish_param = df_wish_param['6 site']

    #print(i)
    #print('mean ', df_wish_param.mean())
    #print('vary ', df_wish_param.var())

    #if (df_wish_param.max() - df_wish_param.min())>2:
    #df_wish_param.plot()


    #df_for_plotting.pivot_table(values='6 site', index='WAFER', fill_value=None,margins=False,dropna=True).plot(label=i)
    df_site = df_for_plotting['6 s']
    df_site.plot()
    plt.title("Parameter in 6 s")
    plt.ylabel('6 s')
    plt.xlabel('L/w')

plt.legend(df_for_plotting['PARAMETER'])
plt.show()
#while True:
 #   i=0
