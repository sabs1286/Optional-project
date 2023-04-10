#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df_data = pd.read_csv('data.csv')
df_data


# In[3]:


x = list (df_data.iloc[:, 0])
y = list (df_data.iloc[:, 1])

plt.bar(x, y, color = 'g')
plt.title("total sales for each year (2012 to2021)")
plt.xlabel("years")
plt.ylabel("number of sales")

plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array (['Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
y = np.array (['-109563.4983', '-104612.8465', '-103008.197', '-87980.17405', '-82480.56325', '-78068.85048'])
plt.title("estimated sales for the last six months (Jul to Dec) of 2022")
plt.xlabel("estimated sales")
plt.ylabel("months")
plt.bar(x,y, width =0.1)
plt.show()


# In[8]:


import matplotlib.pyplot as plt

x = np.array (['Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
y = np.array (['-109563.4983', '-104612.8465', '-103008.197', '-87980.17405', '-82480.56325', '-78068.85048'])

plt.barh(y, x)
plt.title("estimated sales for the last six months (Jul to Dec) of 2022")
plt.xlabel("estimated sales")
plt.ylabel("months")

plt.show()


# In[ ]:




