import pandas as pd
import numpy as np

data = {'impact':[5,5,7,10,5,10,14,15,30,25]}
df = pd.DataFrame(data,index=['a','b','c','d','e','f','g','h','i','j'])

numgroups = 3

group_targetsum = round(df.impact.sum() / numgroups, -1)


a = df.values.ravel()
shift_num = group_targetsum*np.arange(1,numgroups)
idx = np.searchsorted(a.cumsum(), shift_num,'right')
gg = np.split(a, idx)

print("Total will be around:",group_targetsum)
print(gg)
