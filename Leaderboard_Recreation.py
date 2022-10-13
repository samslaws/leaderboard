#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


# In[194]:


df = pd.read_csv('jan19_leaderboard_rough01.csv')


# In[195]:


df['Districts'] = df['Districts'].fillna(0)


# In[196]:


df['Antitrust'] = df['Antitrust'].fillna(0)


# In[197]:


df['Consumer Protection'] = df['Consumer Protection'].str.replace(',', '').astype(float)


# In[198]:


df['Consumer Protection'] = df['Consumer Protection'].fillna(0)


# In[199]:


df['Contracts'] = df['Contracts'].fillna(0)


# In[200]:


df['Copyright'] = df['Copyright'].fillna(0)


# In[201]:


df['Employment'] = df['Employment'].str.replace(',', '').astype(float)


# In[202]:


df['Employment'] = df['Employment'].fillna(0)


# In[203]:


df['Insurance'] = df['Insurance'].fillna(0)


# In[204]:


df['Patent'] = df['Patent'].fillna(0)


# In[205]:


df['Product Liability'] = df['Product Liability'].fillna(0)


# In[206]:


df['Securities'] = df['Securities'].fillna(0)


# In[207]:


df['Torts'] = df['Torts'].str.replace(',', '').astype(float)


# In[208]:


df['Torts'] = df['Torts'].fillna(0)


# In[209]:


df['AggregatedDealvalue'] = df['AggregatedDealvalue'].fillna(0)


# In[210]:


df['Offering Size'] = df['Offering Size'].fillna(0)


# In[211]:


df['prestige_score'] = df['prestige_score'].fillna(0)


# In[212]:


df['sc_final_score_unrd'] = df['sc_final_score_unrd'].fillna(0)


# In[213]:


df['Districts_Perc_Rank'] = df.Districts.rank(pct=True)


# In[214]:


df['Antitrust_Perc_Rank'] = df.Antitrust.rank(pct=True)


# In[215]:


df['Consumer_Protection_Perc_Rank'] = df['Consumer Protection'].rank(pct=True)


# In[216]:


df['Contracts_Perc_Rank'] = df['Contracts'].rank(pct=True)


# In[217]:


df['Copyright_Perc_Rank'] = df['Copyright'].rank(pct=True)


# In[218]:


df['Employment_Perc_Rank'] = df['Employment'].rank(pct=True)


# In[219]:


df['Insurance_Perc_Rank'] = df['Insurance'].rank(pct=True)


# In[220]:


df['Patent_Perc_Rank'] = df['Patent'].rank(pct=True)


# In[221]:


df['Product_Liability_Perc_Rank'] = df['Product Liability'].rank(pct=True)


# In[222]:


df['Securities_Perc_Rank'] = df['Securities'].rank(pct=True)


# In[223]:


df['Torts_Perc_Rank'] = df['Torts'].rank(pct=True)


# In[224]:


df['Case_Type_Volume'] = (df['Antitrust_Perc_Rank'] + df['Consumer_Protection_Perc_Rank'] + df['Contracts_Perc_Rank'] + df['Copyright_Perc_Rank'] + df['Employment_Perc_Rank'] + df['Insurance_Perc_Rank'] + df['Patent_Perc_Rank'] + df['Product_Liability_Perc_Rank'] + df['Securities_Perc_Rank'] + df['Torts_Perc_Rank']) / 10 


# In[225]:


df['MA_Volume'] = df['AggregatedDealvalue'].rank(pct=True)


# In[226]:


df['RO_Volume'] = df['Offering Size'].rank(pct=True)


# In[227]:


df['Work_Score'] = (df['Districts_Perc_Rank'] + df['Case_Type_Volume'] + df['MA_Volume'] + df['RO_Volume']) / 4


# In[228]:


df['leaderboard_score'] = (df['Work_Score'] + df['prestige_score'] + df['sc_final_score_unrd']) / 3


# In[229]:


df['final_leaderboard_score'] = df['leaderboard_score'] * 100


# In[230]:


df.to_csv('jan19_leaderboard_rough01.csv')


# In[ ]:




