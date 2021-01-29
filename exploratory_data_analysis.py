#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("bank_additional.csv", sep=';')


# In[3]:


data.head()


# In[4]:


data = data.drop(["contact", "month", "day_of_week"], axis=1)
data.head()


# In[5]:


data.nunique()


# In[6]:


data["y"].replace(('yes', 'no'), (1, 0), inplace=True)
data.head()


# In[7]:


data.isnull().sum()


# In[8]:


data.describe()


# In[9]:


data.corr()


# In[24]:


sns.relplot(data=data, x='duration', y='previous', hue='y', alpha=0.6)


# In[11]:


# duration affect responses, higher campaign duration has a tendency to get 'yes' response.
# previous campaign reduces duration needed for customer to give 'yes' response.


# In[25]:


sns.relplot(data=data, x='duration', y='pdays', hue='y', alpha=0.6)


# In[13]:


# customers who get campaign in a few previous day have a tendency to give 'yes' response.


# In[26]:


sns.relplot(data=data, x='previous', y='pdays', hue='y', alpha=0.6)


# In[15]:


data.hist(column='job', by='y', bins=23)


# In[16]:


data.hist(column='marital', by='y', bins=10)


# In[17]:


data.hist(column='education', by='y', bins=23)


# In[18]:


data.hist(column='default', by='y', bins=5)


# In[19]:


data.hist(column='housing', by='y', bins=5)


# In[20]:


data.hist(column='loan', by='y', bins=5)


# In[21]:


data.boxplot(column='age', by='y')


# In[22]:


# Analyze how social index affect rensponse


# In[27]:


data.head()


# In[32]:


data.corr()


# In[33]:


sns.relplot(x='emp.var.rate', y='cons.price.idx', hue='y', alpha=0.6, data=data)


# In[34]:


sns.relplot(x='cons.conf.idx', y='euribor3m', hue='y', alpha=0.6, data=data)


# In[37]:


sns.relplot(x='nr.employed', y='emp.var.rate', hue='y', alpha=0.6, data=data)


# In[38]:


# Social index data will be droped since have a low effect on renponse


# In[39]:


data = data.drop(['emp.var.rate','cons.price.idx','cons.conf.idx','euribor3m','nr.employed'], axis=1)
data.head()


# In[40]:


data.to_csv('cleaned_bank_campaign.csv')


# In[ ]:




