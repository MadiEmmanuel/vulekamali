#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)

data = pd.read_csv("provincial-time-series.csv")
data.dropna()
 
data.head(n=2)                   


# In[27]:


EC1 = data[data.government == 'Eastern Cape']
EC = df[EC1]


# In[42]:


EC.dropna()
EC.value.describe()


# In[29]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

data = pd.read_csv("provincial-time-series.csv")
data.dropna()

EC = data[data.government == 'Eastern Cape']
money = EC1.value
prov = EC1.department


# Create a trace
trace = go.Scatter(
    x = prov,
    y = money
)

data = [trace]

iplot(data, filename='basic-line')


# In[31]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

data = pd.read_csv("provincial-time-series.csv")
data.dropna()

EC = data[data.government == 'Eastern Cape']
money = EC1.value
prov = EC1.department

data = [go.Bar(
            x=prov,
            y=money
    )]

iplot(data, filename='basic-bar')


# In[ ]:





# In[14]:


GP = data[data.government == 'Gauteng']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


WC = data[data.government == 'Western Cape']


# In[ ]:


FS = data[data.government == 'Free State']


# In[ ]:


NW = data[data.government == 'North West']


# In[ ]:


KZN = data[data.government == 'KwaZulu-Natal']


# In[ ]:


Mp = data[data.government == 'Mpumalanga']


# In[ ]:


L = data[data.government == 'Limpopo']


# In[ ]:


NC = data[data.government == 'Northen Cape']


# In[ ]:





# In[ ]:





# In[ ]:




