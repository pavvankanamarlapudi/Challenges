#!/usr/bin/env python
# coding: utf-8

# In[161]:


import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)
data = pd.read_csv(r"C:\Users\pavan\Downloads\SP500.csv")


# In[47]:


data.head()


# In[49]:


data['Date'] = pd.to_datetime(data['Date'])


# #### Dataframe to array Conversion

# In[107]:


array_dat = data.to_numpy()


# In[108]:


array_dat[:5]


# #### Q1. The highest daily gain and its date, the highest daily loss and its date,

# In[35]:


## Daily Gain
array_dat[array_dat[:,2]==max(array_dat[:,2])][0,[0,2]]


# In[36]:


## Daily Loss
array_dat[array_dat[:,3]==max(array_dat[:,3])][0,[0,3]]


# #### Q2. The most daily transaction volume and its date,

# In[34]:


array_dat[array_dat[:,-1]==max(array_dat[:,-1])][0,[0,-1]]


# In[29]:


array_dat[array_dat[:,2]==max(array_dat[:,2])]


# #### Q4. a yearly report which has annual average open price, close price, transaction volume and gain/loss from 1950 to 2018, and the most profitable year,

# In[109]:


## year and month derivation from date.
array_dat = np.insert(array_dat,1,[array_dat[i,0].year for i in range(array_dat.shape[0])],1)
array_dat = np.insert(array_dat,1,[array_dat[i,0].month for i in range(array_dat.shape[0])],1)


# In[141]:


array_dat[0]


# In[156]:


year_l,open_price,close_price,vol =[],[],[],[]
for year in np.unique(array_dat[:,2]):
    year_l.append(year)#year
    open_price.append(array_dat[(array_dat[:,2]==year)][:,3].mean())#Open
    close_price.append(array_dat[(array_dat[:,2]==year)][:,7].mean())#Close
    vol.append(array_dat[(array_dat[:,2]==year)][:,-1].mean())#Volume


# In[157]:


yearly_result_array = np.array([year_l,open_price,close_price,vol])
yearly_result_array


# #### Q3. a monthly report for year 2017-2018, which has monthly average open price, close price, transaction volume and gain/loss, and a query to find all of the months which have certain range of open prices

# In[142]:


array_dat


# In[159]:


month_l,monthly_avg_open,monthly_avg_close,monthly_avg_vol =[],[],[],[]
for month in np.unique(array_dat[:,1]):
    month_l.append(month)#year
    monthly_avg_open.append(array_dat[(array_dat[:,1]==month)][:,3].mean())#Open
    monthly_avg_close.append(array_dat[(array_dat[:,1]==month)][:,7].mean())#Close
    monthly_avg_vol.append(array_dat[(array_dat[:,1]==month)][:,-1].mean())#Volume


# In[160]:


monthly_result_array = np.array([month_l,monthly_avg_open,monthly_avg_close,monthly_avg_vol])
monthly_result_array.T


# #### Q5. A every other five year report which has every five year average open price, close price, transaction volume and gain/loss from 1950 to 2018, and the most profitable five year,

# In[164]:


np.set_printoptions(suppress=True)
yearly_result_array  = yearly_result_array.T


# In[173]:


cnt=0
start=1950
while end<2018:
    end=start+5
    print(start,end)
    start=end
    cnt=cnt+1


# In[184]:


yearly_result_array[(yearly_result_array[:,0]>=1950) & (yearly_result_array[:,0]<=1955),1]
yearly_result_array[(yearly_result_array[:,0]>=1950) & (yearly_result_array[:,0]<=1955),2]
yearly_result_array[(yearly_result_array[:,0]>=1950) & (yearly_result_array[:,0]<=1955),3]


# In[192]:


fy_year_l,fy_open_price,fy_close_price,fy_vol =[],[],[],[]
cnt=0
start=end=1950
while end<2018:
    end=start+5
    print(f"{start}-{end} avg computed and saved in array!")
    fy_year_l.append(f"{start}-{end}")
    fy_open_price.append(yearly_result_array[(yearly_result_array[:,0]>=start) & (yearly_result_array[:,0]<=end),1].mean())
    fy_close_price.append(yearly_result_array[(yearly_result_array[:,0]>=start) & (yearly_result_array[:,0]<=end),2].mean())
    fy_vol.append(yearly_result_array[(yearly_result_array[:,0]>=start) & (yearly_result_array[:,0]<=end),3].mean())
    start=end
    cnt=cnt+1


# In[193]:


fiveYear_result_array = np.array([fy_year_l,fy_open_price,fy_close_price,fy_vol])
fiveYear_result_array.T


# In[ ]:




