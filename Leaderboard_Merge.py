#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd

pd.options.display.max_rows = 999
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[74]:


old_lex = pd.read_csv('jan14_lex_old.csv')
new_lex = pd.read_csv('jan14_lex_new.csv')


# In[75]:


lex = old_lex.merge(new_lex, how='outer', on='Law Firm')


# In[76]:


lex.to_csv('jan14_lex.csv')


# In[90]:


prestige = pd.read_csv('clean_jan11_prestige.csv')
social = pd.read_csv('clean_jan11_social.csv')
LM = pd.read_csv('jan14_lex.csv')
MA = pd.read_csv('jan14_ma_clean.csv')
RO = pd.read_csv('jan14_ro_clean.csv')


# **REMOVE ROWS WITHOUT FIRM IDS**

# In[91]:


prestige_social = prestige.merge(social, how='outer', on='firm_id')


# In[92]:


presocialex = prestige_social.merge(LM, how='left', on='firm_id')


# In[93]:


presocialexmerger = presocialex.merge(MA, how='left', on='firm_id')


# In[94]:


final = presocialexmerger.merge(RO, how='left', on='firm_id')


# In[95]:


final.to_csv('jan14_leaderboard_raw.csv')


# In[ ]:





# In[7]:


social_full = pd.read_csv('social_full_score_jan11.csv')
social_impact = pd.read_csv('social_impact_jan11.csv')


# In[8]:


social = social_impact.merge(social_full, how='outer', on='firm_id')


# In[9]:


social.to_csv('social-impact_jan11.csv')


# In[3]:


lex_jan11 = pd.read_csv('lex_jan11.csv')
le = pd.read_csv('leaderboard_merged_jun11.csv')


# In[4]:


final_df = le.merge(lex_jan11, how='outer', on='Law Firm')


# In[5]:


final_df.to_csv('leaderboard_jan11.csv')


# In[3]:


new_lex = pd.read_csv('lex_dec20.csv')
old_lex = pd.read_csv('lex_old.csv')


# In[4]:


final_lex = old_lex.merge(new_lex, how='outer', on='Law Firm')


# In[5]:


final_lex.to_csv('final_lex.csv')


# In[9]:


new_ma = pd.read_csv('new_ma.csv')
old_ma = pd.read_csv('old_ma.csv')


# In[10]:


final_ma = old_ma.merge(new_ma, how='outer', on='LawFirmId')


# In[11]:


final_ma.to_csv('final_ma.csv')


# In[12]:


new_ro = pd.read_csv('new_ro.csv')
old_ro = pd.read_csv('old_ro.csv')


# In[13]:


final_ro = old_ro.merge(new_ro, how='outer', on='Law Firm Id')


# In[14]:


final_ro.to_csv('final_ro.csv')


# In[33]:


prestige = pd.read_csv('prestige_dec15.csv')
prestige_urls = pd.read_csv('prestige_url.csv')


# In[24]:


prestige = pd.read_csv('prestige_dec21.csv')
social = pd.read_csv('social_dec21.csv')
lex = pd.read_csv('lex_clean_dec21.csv')
ma = pd.read_csv('ma_clean_dec21.csv')
ro = pd.read_csv('ro_clean_dec21.csv')


# In[25]:


prestige_social = prestige.merge(social, how='outer', on='firm_id')


# In[26]:


prestige_social.head()


# In[27]:


prestige_social_lex = prestige_social.merge(lex, how='outer', on='firm_id')


# In[28]:


prestige_social_lex_ma = prestige_social_lex.merge(ma, how='outer', on='firm_id')


# In[29]:


prestige_social_lex_intel = prestige_social_lex_ma.merge(ro, how='outer', on='firm_id')


# In[30]:


prestige_social_lex_intel.to_csv('finaldf_clean_dec21.csv')


# In[32]:


df = prestige_social_lex_intel


# In[33]:


df.head()


# In[29]:


socialdf.to_csv('socialdf_urls.csv')


# In[34]:


prestige = pd.read_csv('prestige_dec15.csv')
prestige_urls = pd.read_csv('prestige_url.csv')


# In[35]:


prestigedf = prestige.merge(prestige_urls, how='outer', on='firm_id')


# In[36]:


prestigedf.to_csv('prestigedf_urls.csv')


# In[21]:


ma = pd.read_csv('clean_ma.csv')
ro = pd.read_csv('clean_ro.csv')
df = pd.read_csv('clean_merged.csv')


# In[14]:


ldb = pd.read_csv('leaderboard_minus_ma.csv')


# In[15]:


prestige = pd.read_csv('prestige_dec.csv')
social = pd.read_csv('social_dec.csv')
lex = pd.read_csv('lex_dec.csv')


# In[16]:


prestige_social = prestige.merge(social, how='outer', on='firm_id')


# In[22]:


ma_df = df.merge(ma, how='outer', on='firm_id')


# In[24]:


ma_df_ro = ma_df.merge(ro, how='outer', on='firm_id')


# In[25]:


ma_df_ro.to_csv('dec14_final.csv')


# In[59]:


leaderboard = pd.read_csv('filtered_leaderboard.csv', index_col=0)


# In[16]:


everything.to_csv('everything.csv')


# In[35]:


df.head()


# In[50]:


df = pd.read_csv('leaderboard_jan6.csv')


# In[23]:


df


# In[21]:


type(df['case_type_count_log-min-max'][0])


# In[26]:


df['case_type_count_log-min-max'][:265]


# In[27]:


df['case_type_count_log-min-max'][:265] = df['case_type_count_log-min-max'][:265].astype(float)


# In[54]:


df.hist(column='Geo_Reach_Log_Min-Max')


# In[49]:


df.hist(column='Value_per_offering_perc_rank')


# In[15]:


df.hist(column='case_type_count_min-max')


# In[ ]:





# In[ ]:





# In[36]:


df.hist(column='Districts')


# In[42]:


df.hist(column='Antitrust')


# In[48]:


df['Consumer Protection'] = df['Consumer Protection'].replace(',','', regex=True)


# In[51]:


df['Consumer Protection'] = df['Consumer Protection'].apply(pd.to_numeric,errors='coerce')


# In[52]:


df.hist(column='Consumer Protection')


# In[53]:


df.hist(column='Contracts')


# In[56]:


df['Employment'] = df['Employment'].replace(',','', regex=True)
df['Employment'] = df['Employment'].apply(pd.to_numeric,errors='coerce')


# In[57]:


df.hist(column='Employment')


# In[58]:


df.hist(column='Insurance')


# In[59]:


df.hist(column='Patent')


# In[60]:


df.hist(column='Product Liability')


# In[61]:


df.hist(column='Securities')


# In[65]:


df.hist(column='Copyright')


# In[63]:


df['Torts'] = df['Torts'].replace(',','', regex=True)
df['Torts'] = df['Torts'].apply(pd.to_numeric,errors='coerce')


# In[64]:


df.hist(column='Torts')


# In[66]:


catdf = df[['Antitrust', 'Consumer Protection', 'Contracts', 'Copyright', 'Employment', 'Insurance', 'Patent', 'Product Liability', 'Securities', 'Torts']]


# In[68]:


catdfcorr = catdf.corr()


# In[79]:


catdfcorr.sort_values(by='Torts', ascending=False)


# In[80]:


df.hist(column='AggregatedDealvalue')


# In[81]:


df.hist(column='DealCount')


# In[82]:


df.hist(column='Offering Size')


# In[83]:


df.hist(column='Last Offerings Count')


# In[86]:


dfl = pd.read_csv('leaderboard_raw_dec23.csv')


# In[85]:


dfl.hist(column='Workhorse')


# In[87]:


dfl.hist(column='Geo_Reach')


# In[88]:


dfl.hist(column='case_type_count')


# In[89]:


dfl.hist(column='type_avg_10')


# In[90]:


dfl.hist(column='Value_per_Deal')


# In[91]:


dfl.hist(column='Value_Per_Offering')


# In[95]:


dfl = pd.read_csv('leaderboard_log_minmax.csv')


# In[93]:


dfl.hist(column='Geo_Reach_Log')


# In[96]:


dfl.hist(column='Geo_Reach_Log_Min-Max')


# In[61]:


state_list = []
i = 0
for x in leaderboard['States / Territories Names']:
    if isinstance(leaderboard['States / Territories Names'][i], float) == True:
        i += 1
        pass
    else:
        state_string = leaderboard['States / Territories Names'][i]
        sample_state_list = state_string.split(",")
        state_list.append(sample_state_list)
        i += 1


# In[24]:


test_string = prestige_social_lex['States / Territories Names'][0]


# In[25]:


test_list = test_string.split(",")


# In[52]:


state_list[283]


# In[63]:


state_list


# In[64]:


result = sum(state_list, [])


# In[87]:


clean_states = []
for x in result:
    state = x.lstrip(' ')
    clean_states.append(state)


# In[88]:


clean_states


# In[89]:


from collections import Counter


# In[90]:


Counter(clean_states)


# In[53]:


prestige_social_lex['States / Territories Names']


# In[13]:


lex_and_key_1 = lex_and_key.dropna(subset=['Total Cases'])


# In[14]:


lex_and_key_1.to_csv('lex_data_key_1.csv')


# In[17]:


prestige_index = index.merge(prestige_key, how='outer', on='firm_id')


# In[21]:


prestige_key_index = prestige_index.merge(prestige, how='outer', on='Firm Name')


# In[35]:


prestige_key_index.head()


# In[22]:


social.head()


# In[36]:


prestige_social = prestige_key_index.merge(social, how='outer', on='firm_id')


# In[37]:


prestige_social


# In[25]:


lex.head()


# In[26]:


non_firms = ['Department of Justice', 'Equal Employment Opportunity Commission', 'United States Department of Labor', 'Securities and Exchange Commission', 'State of New York', 'State of Texas', 'State of Maryland', 'State of California', 'State of Illinois', 'State of Michigan', 'State of Florida', 'State of Washington', 'State of Ohio', 'State of Pennsylvania', 'State of New Jersey', 'City of New York, New York', 'City of Chicago, Illinois', 'City of Philadelphia, Pennsylvania', 'California Department of Justice']


# In[27]:


lex = lex[~lex['Law Firm'].isin(non_firms)]


# In[38]:


prestige_social = prestige_social.rename(columns={"Law360 Formatted Name": "Law Firm"})


# In[39]:


prestige_social_lex = prestige_social.merge(lex, how='outer', on='Law Firm')


# In[42]:


prestige_social_lex.head()


# In[ ]:





# In[ ]:





# In[106]:


madf


# In[107]:


madf.sort_values(by=['DealCount'], ascending=False)


# In[108]:


rodf


# In[110]:


rodf.sort_values(by=['Last Offerings Count'], ascending=False)


# In[40]:


rodf = rodf.rename(columns={"Law Firm Name": "Lawfirm"})


# In[41]:


newdf = madf.merge(rodf, how='outer', on='Lawfirm')


# In[46]:


newdf.head()


# In[48]:


newdf = newdf.rename(columns={"Lawfirm": "Law Firm"})


# In[49]:


finaldf = prestige_social_lex.merge(newdf, how='outer', on='Law Firm')


# In[50]:


finaldf.to_csv('finaldf.csv')


# In[ ]:





# In[39]:


newdf.to_csv('intelldf.csv')


# In[27]:


newdf = pd.read_csv('intelldf.csv', index_col=0)


# In[102]:


newdf


# In[105]:


newdf.sort_values(by=['Last Offerings Count'], ascending=False)


# In[3]:


geo = pd.read_csv('geographic.csv')


# In[14]:


geo['Law Firm']


# In[111]:


geo


# In[20]:


remove_list = ['Department of Justice', 'City of New York, New York', 'California Department of Justice', 'State of New York', 'State of Texas', 'City of Chicago, Illinois', 'State of Pennsylvania', 'State of New Jersey', 'Carnival Cruise Lines', 'State of Illinois', 'City of Philadelphia, Pennsylvania', 'Royal Caribbean Cruises', 'State of Florida', 'State of Michigan', 'State of District of Columbia', 'State of Ohio', 'State of Maryland', 'State of Washington', 'Securities and Exchange Commission', 'United States Department of Labor', 'Equal Employment Opportunity Commission', 'JAMS']


# In[21]:


newgeo = geo[~geo['Law Firm'].isin(remove_list)]


# In[22]:


newgeo


# In[23]:


newgeo = newgeo.rename(columns={"Law Firm": "Lawfirm"})


# In[40]:


lexintel2 = newdf.merge(newgeo, how='outer', on='Lawfirm')


# In[101]:


lexintel


# In[99]:


lexintel2


# In[42]:


lexintel2.to_csv('lexintel.csv')


# In[43]:


pres = pd.read_csv('prestige.csv')


# In[45]:


pres.head()


# In[46]:


newpres = pres.rename(columns={"Firm Name": "Lawfirm"})


# In[47]:


leaderboard = lexintel2.merge(newpres, how='outer', on='Lawfirm')


# In[48]:


leaderboard


# In[49]:


leaderboard.to_csv('leaderboard.csv')


# In[50]:


index = pd.read_csv('index.csv')


# In[51]:


index.head()


# In[52]:


index = index.rename(columns={"Law360 Formatted Name": "Lawfirm"})


# In[53]:


leaderboard2 = leaderboard.merge(index, how='outer', on='Lawfirm')


# In[54]:


leaderboard2


# In[55]:


leaderboard2.to_csv('leaderboard2.csv')


# In[56]:


maindf = pd.read_csv('leader_raw.csv')


# In[57]:


prekey = pd.read_csv('prestige_key.csv')


# In[58]:


prestige_new = pd.read_csv('prestige11-10.csv')


# In[59]:


social = pd.read_csv('social_impact.csv')


# In[60]:


maindf.head()


# In[61]:


prekey.head()


# In[62]:


prestige_new.head()


# In[63]:


prestige = prestige_new.merge(prekey, how='outer', on='Firm Name')


# In[64]:


prestige.head()


# In[65]:


index.head()


# In[67]:


index = index.rename(columns={"firm_ID": "firm_id"})


# In[68]:


prestige = prestige.merge(index, how='outer', on='firm_id')


# In[71]:


index.head()


# In[69]:


prestige.head()


# In[73]:


prestige = prestige.rename(columns={"Law Firm Graphics Name": "firm_name"})


# In[ ]:





# In[75]:


social_prestige = prestige.merge(social, how='outer', on='firm_name')


# In[70]:


social.head()


# In[76]:


social_prestige


# In[77]:


maindf.head()


# In[80]:


maindf = maindf.rename(columns={"firm_ID": "firm_id"})


# In[81]:


final = social_prestige.merge(maindf, how='outer', on='firm_id')


# In[83]:


pd.set_option('display.max_columns', None)


# In[84]:


final.head()


# In[85]:


final.to_csv('finaldf.csv')


# In[92]:


df = pd.read_csv('almost.csv')


# In[94]:


df.head()


# In[93]:


df.columns = df.iloc[0]


# In[ ]:





# In[88]:


index.head()


# In[95]:


final2 = df.merge(index, how='outer', on='firm_id')


# In[96]:


final2.head()


# In[97]:


final2 = final2.iloc[1: , :]


# In[98]:


final2.to_csv('final2.csv')


# In[ ]:




