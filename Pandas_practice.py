
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


exam_data = {'name': ['anastasia', 'Catherine', 'Cahill', 'James','Emily','Michael','Monica','Laura','Kevin','Jordan'],
            'score': [13,9.5,16.5,np.nan,11,20,17,np.nan,8.5,19],
             'attempts': [1,3,3,2,2,3,2,3,2,1],
            'qualify': ['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data, index=labels)


# In[3]:


df


# In[19]:


#1-1
df.loc[:,['name','score']]


# In[15]:


#1-2
df.iloc[:3,:1]


# In[21]:


#1-3
df.loc[['a','b','e','f'],['name','score']]


# In[23]:


#1-3
df.iloc[[0,1,4,5],:2]


# In[25]:


#1-4
df[df['attempts']>2]


# In[35]:


#2-1
df[df['score'].isnull()]


# In[44]:


#2-2
df[df['attempts']<2][df['score']>15]


# In[47]:


#2-3
df['attempts'].sum()


# In[48]:


#2-4
df['score'].mean()


# In[50]:


df


# In[78]:


#3-1
data ={'name':'Saya','score':17.5,'attempts':2,'qualify':'yes'}
label=['k']
df1 = pd.DataFrame(data,index=label)
df = df.append(df1)
df


# In[79]:


#3-2
df = df.drop('k',axis=0)
df


# In[80]:


#3-3
df.drop('attempts',axis=1)


# In[83]:


#3-4
df.groupby('attempts').score.sum()


# In[84]:


#4
df


# In[31]:


exam2_data = {'name': ['anastasia', 'Catherine', 'Cahill', 'James','Emily','Michael','Monica','Laura','Kevin','Jordan'],
              'score2': [11,20,16.5,np.nan,10,15,20,np.nan,8,8]}
labels2 = ['a','b','c','d','e','f','g','h','i','j']

df2 = pd.DataFrame(exam2_data, index=labels2)
df2


# In[33]:


df3 = df.set_index('name').join(df2.set_index('name'), how='inner')
df3

