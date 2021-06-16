import pandas as pd

#creation dictionary
dict_cities={'City':['Moscow','Saint-Petersburg','Nvosibirsk'],'Population':[126078,454455,788113]}
#creation Dataframe
df = pd.DataFrame(dict_cities)
#print(df)

#creation excel from dataframe
df.to_excel('cities.xlsx')

#creation list
list1=[['Moscow','Saint-Petersburg','Nvosibirsk'],[126078,454455,788113]]
#creation datframe from list
df=pd.DataFrame(list1).T #change columns and rows
#print(df)

# creation dataframe form csv file
#df=pd.read_csv('гиперссылка на файл или путь на компе')
#df.head(15)  первые 15 строк
#df.tail(15)  последние 15 строк
#df.info info about types of information
#df.describe  statistical information  df.describe(include='all') all information
#df.shape quantity of rows and columns

#choose of columns  los - choose by name, iloc -choose by number

df=pd.read_excel('cities.xlsx')
#Call to the column by Name
#print(df.City)
#print(df['City'])
#Call to several columns
#print(df[['City','Population']])
#Call  to  several columns and rows
print(df.loc[2:3,'City':'Population']) #show all information
print (df.iloc[1:2,1:2])  #doesnt't show the right position (-1)

#definition
#df[df['sex']=='Both']
#combination of definitions
#df[(df['sex]=='Both'& df['']=''& df['']==''>600)]
#cardio=df[(df['sex]=='Both'& df['']=''& df['']==''>600)] # save our dtaframe to new dataframe
#cardio.sort_values(by=['val'],ascending=False) # sorting by the column 'val'
#find the information which contains some word
#df[df['cause'].str.contains('HIV')] если нужна информация, не содержащая слов, то df[df['cause'].str.contains('HIV')==False]

#delete column
#df.drop('name of column', axis=1, inplace= True (внести изменения в начальный датафрэйм))
#df.drop('name of column','name of column', axis=1, inplace= True (внести изменения в начальный датафрэйм))