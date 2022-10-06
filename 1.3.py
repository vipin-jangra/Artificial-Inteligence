import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

df = pd.read_csv("titanic_original.csv",skip_blank_lines=True)
data = round((df['sex'].value_counts())/len(df)*100,2)

labels = ['male', 'Female']
sizes = data.tolist()

fig, (ax,ax2) = plt.subplots(1,2)
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Male/Female proportion')

colors = {'male':'blue', 'female':'orange'}

    
ax2.scatter(df.name.astype(str),df.sex.astype(str),c = df['sex'].iloc[:-1].apply(lambda x: 
    colors[x]))
ax2.set_xlabel('Fare')
ax2.set_ylabel('Age')
ax2.set_title('Fare paid and the Age')






