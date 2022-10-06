import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
fig = plt.subplots(figsize =(12, 8))
barWidth = 0.25



df = pd.read_csv("sales (2).csv")
w1 = df['week 1 '].tolist()
w2 = df['week 2'].tolist()
w3= df ['week3'].tolist()


br1 = np.arange(len(w1))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
plt.bar( br1,w1, color ='r', width = barWidth ,linewidth=2, linestyle = 'dashed', 
        edgecolor ='purple', label ='w1')
plt.bar( br2,w2, color ='g', width = barWidth, linewidth=2, linestyle = 'dashed',
        edgecolor ='grey', label ='w2')
plt.bar( br3,w3, color ='b',width = barWidth, linewidth=2, linestyle = 'dashed',
        edgecolor ='grey', label ='w3')
 
# Adding Xticks
plt.xlabel('DAY')
plt.ylabel('SALES(in Rs)')
plt.xticks([r + barWidth for r in range(len(w1))],
        ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY','SATURDAY','SUNDAY'])
 
plt.legend()
plt.show()