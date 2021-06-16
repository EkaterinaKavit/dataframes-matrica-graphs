import  pandas as pd
df = pd.read_excel('first_try_excel.xlsx')

#print(df.sort_values(['Std Deviation'],ascending=False))
df_dev=df.nlargest(5,'Std Deviation')
#print(df_dev)
df_dev.to_excel('std.dev.xlsx')
df.groupby('Lot')
import matplotlib.pyplot as plt
df[(df['WAFER']==2)&(df['Lot']=="M030031_FIN")].pivot_table(values='Std Deviation', index='PARAMETER',fill_value=None,margins=False,dropna=True).plot(kind='line')
plt.ylabel('Std.deviation per wafer')
plt.title('My first graph')