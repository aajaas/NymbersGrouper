import pandas as pd
import numpy as np

data = {'impact':[5,5,7,10,5,10,14,15,30,25]}
df = pd.DataFrame(data,index=['a','b','c','d','e','f','g','h','i','j'])

numgroups = 3

group_targetsum = round(df.impact.sum() / numgroups, -1)

df['csum'] = df['impact'].cumsum()
df['csum_midpoint'] = (df.csum + df.csum.shift().fillna(0)) / 2.

df['group'] = pd.cut( df.csum_midpoint, np.linspace(0,df['impact'].sum(),numgroups+1 ))
gg = df.groupby( df.group )['impact'].sum()

print("Total will be around:",group_targetsum)
print(gg)
