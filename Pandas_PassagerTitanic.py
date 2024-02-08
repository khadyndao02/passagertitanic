import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import optimize
from scipy import signal
from scipy import fftpack
from scipy import ndimage
import pandas as pd
import time





data = pd.read_excel('titanic3.xls')
print(data)
print("Tabbleau",data.corr())
data.loc[data['age']<= 20, 'age']=0
data.loc[(data['age']>20)& (data['age']<= 30), 'age']=1
data.loc[(data['age']>30)& (data['age']<= 40), 'age']=2
data.loc[data['age']>40, 'age']=3
print(data.head())
print(data['age'].value_counts())
print(data.groupby(['age']).mean())


print(data.shape)
print(data.columns)
print(data.head())# les premiers lignes
data = data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest'],axis = 1)#supprimer une colonne
print(data)
print(data.head)
def category_age(age):
    if age <=20:
        return '<20'
    elif (age>20)&(age<=30):
        return '20-30 ans'
    elif (age>30)&(age <= 40):
        return '30-40 ans'
    else :
        return '+40 ans'
print(data['age'].map(category_age))
print(data['sex'].astype('category'))
print(data['sex'].replace(['male','female'],[0,1]))

print(data.describe())#analyse
data = data.dropna(axis = 0) #eliminer des lignes
print(data)
print(data.describe())
print(data.shape)
data1 = data['pclass'].value_counts()
print(data1)
data1.plot.bar()
plt.show()
data['age'].hist()
plt.show()
Groupe =data.groupby(['sex']).mean()
print(Groupe)
Group =data.groupby(['sex','pclass']).mean()
print(Group)

#localisation par indexing
print(data.iloc[0:2,0:2])
print(data.loc[0:2,'age'])
#DataFrame et Series
print(data['age'][0:10])#indexing

print(data['age']<18)#mask
print(data[data['age']<18].groupby(['sex','pclass']).mean())
print(data[data['age']<18]['pclass'].value_counts())
data = data.set_index('sex')
print(data['age'])




