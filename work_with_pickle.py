import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wish_parameters = ['BNN1010BTA', 'BNN1010BV']
#wish_parameters = ['EN1000P2', 'EN1000V']

# сравнить пвг на участках корреляции параметров и малой дисперсии  и   на участках рассинхрона параметров и большой дисперс (см принт 00:42)
#wish_parameters = ['EN100M1', 'EN100M3', 'EN100X3', 'EN50CUM']


#df=pd.read_excel('F8_PT_32kp_2.xlsx', engine='openpyxl')
#df.to_pickle('F8_32_2.pickle')
df1 = pd.read_pickle('F8_32_2.pickle')

for i in wish_parameters:
#for i in set(df1['PARAMETER'].tolist()):
    df_for_plotting = df1[df1['PARAMETER'] == i]
    #df_for_plotting = df_for_plotting[300:700]

    #df_for_plotting = df1[df1['PARAMETER'] == 'DNEPMMUL']
    #df_wish_param = df_for_plotting[(df_for_plotting['6 site']<150) & (df_for_plotting['6 site']>-30)]
    #df_wish_param = df_wish_param['6 site']

    #print(i)
    #print('mean ', df_wish_param.mean())
    #print('vary ', df_wish_param.var())

    #if (df_wish_param.max() - df_wish_param.min())>2:
    #df_wish_param.plot()


    #df_for_plotting.pivot_table(values='6 site', index='WAFER', fill_value=None,margins=False,dropna=True).plot(label=i)
    df_site = df_for_plotting['6 site']
    df_site.plot()
    plt.title("Parameter in 6 site")
    plt.ylabel('6 site')
    plt.xlabel('Lots and wafers')

plt.legend(df_for_plotting['PARAMETER'])
plt.show()
#while True:
 #   i=0
