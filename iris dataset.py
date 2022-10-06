# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:36:34 2022

@author: vipin
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dat = pd.read_csv("iris_csv.csv")
print(dat)
dat.info()

counts = dat['class'].value_counts()
print(counts)

sepal_length = dat['sepallength'].describe()
print(sepal_length)

sepal_width = dat['sepalwidth'].describe()
print(sepal_width)

petal_length = dat['petallength'].describe()
print(petal_length)

petal_width = dat['petalwidth'].describe()
print(petal_width)

clas = dat['class'].describe()
print(clas)

#sepal length histogram
plt.hist(dat['sepallength'])
plt.ylabel('No of items')
plt.show()

#sepal width histogram
plt.hist(dat['sepalwidth'])
plt.ylabel('No of items')
plt.show()

#petal length histogram
plt.hist(dat['petallength'])
plt.ylabel('No of items')
plt.show()

#petal width histogram
plt.hist(dat['petalwidth'])
plt.ylabel('No of items')
plt.show()

#scatterplot of relationship between 
plt.figure(figsize=(16,9))
plt.title('Comparison between various species based on petal length and width')
sns.scatterplot(dat['petallength'],dat['petalwidth'],hue=dat['class'],s=50)

#boxplot
axes = plt.subplots(2,2,figsize = (16,9))
sns.boxplot(y="petalwidth",x = "class", data = dat , orient= 'v', ax = axes[0,0])

axes = plt.subplots(2,2,figsize = (16,9))
sns.boxplot(y="petallength",x = "class", data = dat , orient= 'v', ax = axes[0,0])

axes = plt.subplots(2,2,figsize = (16,9))
sns.boxplot(y="sepallength",x = "class", data = dat , orient= 'v', ax = axes[0,0])

axes = plt.subplots(2,2,figsize = (16,9))
sns.boxplot(y="sepalwidth",x = "class", data = dat , orient= 'v', ax = axes[0,0])
