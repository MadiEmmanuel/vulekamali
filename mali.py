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

def EC(*args):
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
    
print(EC()) 


GP1 = data[data.government == 'Gauteng']
GP = df[GP1]

def GP(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    GP1 = data[data.government == 'Gauteng']
    money = GP1.value
    prov = GP1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(GP()) 

# In[ ]:
WC1 = data[data.government == 'Western Cape']
GP = df[WP1]
# In[ ]:

def WP(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    WC1 = data[data.government == 'Western Cape']
    money = WC1.value
    prov = WC1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(WP()) 

# In[ ]:

FS1 = data[data.government == 'Free State']
FS = df[FS1]
def FS(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    FS1 = data[data.government == 'Free State']
    money = FS1.value
    prov = FS1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(FS())


# In[ ]:

NW1 = data[data.government == 'North West']
NW = df[NW1]

def NW(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    NW1 = data[data.government == 'North West']
    money = NW1.value
    prov = NW1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(FS())

# In[ ]:

KZN1 = data[data.government == 'KwaZulu-Natal']
NW = df[KZN1]

# In[ ]:


def Mp(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    Mp1 = data[data.government == 'Mpumalanga']
    money = Mp1.value
    prov = Mp1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(Mp())

# In[ ]:

L1 = data[data.government == 'Limpopo']
NW = df[L1]

# In[ ]:

def L(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    L1 = data[data.government == 'Limpopo']
    money = L1.value
    prov = L1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(L())


# In[ ]:


NC1 = data[data.government == 'Northen Cape']
NC = df[NC1]

# In[ ]:
def L(**args):
    import pandas as pd
    import plotly.graph_objs as go
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

    data = pd.read_csv("provincial-time-series.csv")
    data.dropna()

    L1 = data[data.government == 'Northen Cape']
    money = L1.value
    prov = L1.department

    data = [go.Bar(
            x=prov,
            y=money
         )]

    iplot(data, filename='basic-bar')
    
print(L())






# In[ ]:





# In[ ]:




