#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('Leaderboard2_Experiment.csv')


# In[3]:


df.head()


# In[4]:


df = df.dropna(subset=['Districts Names', 'States / Territories Names'])


# In[5]:


states = []
for x in df['States / Territories Names']:
    splitted = x.split(',')
    states.append(splitted)
    joined_states = sum(states, [])


# In[6]:


final_states = []
for x in joined_states:
    stripped = x.lstrip()
    final_states.append(stripped)


# In[7]:


states = set(final_states)


# In[8]:


states


# In[9]:


len(states)


# In[10]:


df = df.reset_index(drop=True)


# In[ ]:


df['States / Territories Names']


# In[11]:


states = []
i = 0
for x in df['States / Territories Names']:
    df['States / Territories Names'][i] = df['States / Territories Names'][i].split(', ')
    i += 1


# In[12]:


for x in df['States / Territories Names']:
    print(x)


# In[13]:


mid_atlantic = ['New York', 'New Jersey', 'Pennsylvania', 'Delaware', 'Maryland', 'District of Columbia', 'Virginia', 'West Virginia']
midwest = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'Ohio', 'Wisconsin', 'North Dakota', 'South Dakota']
mountain = ['Arizona', 'Colorado', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming']
new_england = ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut']
non_contiguous = ['Alaska', 'Hawaii', 'Guam', 'Northern Mariana Islands', 'Virgin Islands']
pacific = ['Idaho', 'Oregon', 'Washington', 'California']
south = ['Louisiana', 'Arkansas', 'Alabama', 'Tennessee', 'Kentucky', 'Oklahoma', 'Mississippi', 'Texas']
south_atlantic = ['North Carolina', 'South Carolina', 'Florida', 'Georgia']


# In[107]:


regions = []


# In[52]:


mid_atlantic_region_bool = []
for x in df['States / Territories Names']:
    i = 0
    for state in x:
        if state in mid_atlantic:
            mid_atlantic_region_bool.append(1)
            print(i)
            print(len(x))
            print(state)
            break
        elif i <= len(x):
            print(i)
            i += 1
            print(len(x))
            continue
        else:
            mid_atlantic_region_bool.append(FALSE)
            print("None")
        
        


# In[ ]:


mid_atlant


# In[47]:


mid_atlantic_region_bool = []
for x in df['States / Territories Names']:
    i = 0
    for state in x:
        print(state)
#         if state in mid_atlantic:
#             mid_atlantic_region_bool.append(1)
#             i += 1
#             print(len(state))
#             print(state)
#             break
#         elif i <= len(state):
#             i += 1
#             continue
#         else:
#             mid_atlantic_region_bool.append(0)
#             print(len(state))
#             print("None")


# In[53]:


len(df['States / Territories Names'])


# In[54]:


len(mid_atlantic_region_bool)


# In[55]:


mid_atlantic_region_bool


# In[ ]:




