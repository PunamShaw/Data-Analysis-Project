import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('911.csv')

#print df['zip'].value_counts().head(5)
#print df['twp'].value_counts().head(5)

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
"""
print df['Reason'].value_counts()
sns.countplot(x='Reason',data=df,palette='viridis')
sns.plt.show()
"""
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
#sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
#sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
#dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
#dayHour.head()
#plt.figure(figsize=(12,6))
#sns.heatmap(dayHour,cmap='viridis')
#sns.clustermap(dayHour,cmap='viridis')
dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()
#plt.figure(figsize=(12,6))
#sns.heatmap(dayMonth,cmap='viridis')
sns.clustermap(dayMonth,cmap='viridis')
sns.plt.show()