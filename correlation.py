import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

x=np.arange(10,20)
print(x)
y=np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
print(y)

r=np.corrcoef(x,y) # 0.76 - Pearson correlation coefficient for x and y
print(r)

r1=scipy.stats.pearsonr(x,y) #Pearson's correlation
print(r1)

r2=scipy.stats.spearmanr(x,y) #Spearman's correlation
print(r2)

r3=scipy.stats.kendalltau(x,y) #Kendall's correlation
print(r3)