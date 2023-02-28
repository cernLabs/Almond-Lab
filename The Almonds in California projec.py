
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#from __future__ import print_function # adds compatibility tp python 2 


# In[2]:


import xlrd


# In[3]:


import csv


# <p style="font-size:23px">let's get XLS files on board</p>

# In[4]:


!pip install xlrd


# <p style="font-size:23px">nice! now that we got xlrd in the computer, let's never run this line again</p> 

# In[5]:


df_alm = pd.read_csv('theAlmonds/ALMONDS-AcreageYieldProductionandPrice-2021-04-04.csv')

df_alm


# In[6]:


df_alm.drop(['LOCATION'],axis=1,inplace=True) # California is already a given

df_alm


# In[7]:


# Let's drop more unnecessary columns

df_alm.drop(['STATE ANSI','ASD CODE','COUNTY ANSI','REFERENCE PERIOD'],axis=1, inplace=True)

df_alm


# <p style="font-size:23px"> let's add a "PRODUCTION in kg" column</p>
# 

# In[8]:


df_alm.replace(' ', np.nan, inplace=True)

df_alm


# In[9]:


# this is to get rid of pesky commas and turn the column objects into floats

df_alm['PRODUCTION in LB'] = df_alm['PRODUCTION in LB'].str.replace(',','').astype(float) 

df_alm


# In[10]:



df_alm['PRODUCTION in kg'] = df_alm['PRODUCTION in LB']*0.453592 # 1 lb for every 0.453592 kg

df_alm



# In[11]:


# let's create a new dataframe to graph from 
alm_ykg = pd.DataFrame()


# In[12]:


alm_ykg['year'] = df_alm['YEAR']
alm_ykg['Production in kg'] = df_alm['PRODUCTION in kg']

alm_ykg


# In[13]:


# let's change years to integers

alm_ykg['year'] = alm_ykg['year'].astype(int)

alm_ykg


# <p style="font-size:23px"> now we need to get rid of the repeating years</p>

# In[14]:


alm_ykg = alm_ykg.drop_duplicates(subset=['year'],keep="last")


# <p style="font-size:23px"> let's get the years in order; using .sort_by</p>

# In[15]:


alm_ykg = alm_ykg.sort_values(by=['year'], ascending= True)

alm_ykg


# <p style="font-size:23px"> let's normalize that 1997 value</p>

# In[16]:


alm_ykg = alm_ykg.set_index('year')
alm_ykg


# In[17]:


#alm_ykg['Production in kg'][1997] = (alm_ykg['Production in kg'][1996]+alm_ykg['Production in kg'][1998])*0.5

#alm_ykg

for i in range(alm_ykg['Production in kg']):
 if alm_ykg['Production in kg'][i].isna():
  alm_ykg['Production in kg'][i] = (alm_ykg['Production in kg'][i-1]+alm_ykg['Production in kg'][i+1])*0.5
 else:
  pass

  
 


# <p style="font-size:23px">now let's visualize</p>

# In[18]:


alm_ykg.plot()


# In[19]:


mpl.style.use('ggplot') # remember this. It's so cool to use


# In[20]:


alm_ykg.plot(kind='line',legend =None, figsize=(22,14))


plt.title('kilogram of Almonds produced by year in California')
plt.ylabel('kg in billions')
plt.xlabel('years')


# In[31]:


alm_ykg.plot(kind='bar', alpha = .5, color = 'red', legend =None, figsize=(20,14))


plt.title('kilogram of Almonds produced by year in California')
plt.ylabel('kg in billions')
plt.xlabel('years')


# In[32]:


# barh makes the bar graph horizontal

alm_ykg.plot(kind='barh', alpha = .5, color = 'red', legend =None, figsize=(20,14))


plt.title('kilogram of Almonds produced by year in California')
plt.ylabel('kg in billions')
plt.xlabel('years')


# In[22]:


alm_ykg.plot(kind='area', alpha = 0.5, color = 'red', legend =None, figsize=(16,10)) # code #efdecd is almond :)



plt.title('kilogram of Almonds produced by year in California')
plt.ylabel('kg in billions')
plt.xlabel('years')


# <p style="font-size:23px"> now let's go sales </p>

# In[23]:


df_alm


# In[24]:


df_alm['PRICE RECEIVED in $ / LB'] = df_alm['PRICE RECEIVED in $ / LB'].astype('float')
df_alm


# In[25]:


# create new column for price recieved in kg

df_alm['PRICE RECEIVED in $ / kg'] = df_alm['PRICE RECEIVED in $ / LB'] *0.453592

df_alm.head()


# In[26]:


# create money generated for the year

df_alm['years sales'] = df_alm['PRODUCTION in kg']*df_alm['PRICE RECEIVED in $ / kg']

df_alm


# In[27]:


df_yys = pd.DataFrame()

df_yys['year'] = df_alm['YEAR']
df_yys['years sales'] = df_alm['years sales']

df_yys


# In[28]:


df_yys.dropna(axis=0)


# In[29]:


#looks like we have no data

