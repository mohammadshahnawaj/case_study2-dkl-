#!/usr/bin/env python
# coding: utf-8

# ## Importing required library

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# ## Reading my csv file

# In[2]:


df=pd.read_csv("C:/Users/shahn/Downloads/flipkart_after_eda.csv")
df


# ## understanding the data

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.describe().T


# ## In this data there are total 1008 rows and 13 column are available

# ## checking null values and it's percentage each column wise

# In[7]:


df.isnull().sum()


# In[8]:


df.isnull().mean()*100


# ## Checking attributes datatype

# In[9]:


df.dtypes


# ## distributing data in numerical and categorical columns

# In[10]:


numerical=df.select_dtypes('O')
categorical=df.select_dtypes(exclude="O")


# In[11]:


numerical


# In[12]:


categorical


# ## checking memory usage by this data

# In[13]:


df.memory_usage()


# ## checking all unique phones available in this data

# In[14]:


df.Product_Name.unique()


# In[15]:


df.Product_Name.value_counts()


# In[16]:


df.Product_Name.nunique()


# In[17]:


df.rating.nunique()


# In[18]:


df.ram_size.nunique()


# In[19]:


df.rom_size.nunique()


# In[20]:


df.battery_in_mAh.nunique()


# In[21]:


df.warranty_in_months.nunique()


# In[22]:


df.expanded_memory.nunique()


# ### There are total 769 items available
# phones are available in 33 different ram_size and 28 different rom_size, 
# Maximum warranty year for the phones is 24 months 

# In[23]:


df.head()


# ## Finding the phones which have maximum battery power

# In[24]:


df[["Product_Name","battery_in_mAh"]].reset_index().sort_values(["battery_in_mAh"],ascending=False,ignore_index=True).head(10)


# ## Finding the top 10 phones which have battery power in between < 4000 and > 1000

# In[25]:


battery_power =df[(df['battery_in_mAh']<4000) & (df['battery_in_mAh']>1000)]
result1=battery_power[["Product_Name","battery_in_mAh"]].head(10)
result1


# In[26]:


result1.plot.bar("Product_Name","battery_in_mAh",color=(['g','c']),width=0.3)
font1={"color":"black"}
plt.ylabel('Battery Power',fontsize=16,fontdict=font1)
plt.xlabel('Phone',fontsize=14,fontdict=font1)
plt.grid()
plt.show()


# ## Top 10 Mobile Phones which have maximum discount

# In[27]:


max_disc=df.groupby(["Product_Name",'discount']).sum().reset_index().sort_values(['discount'],ascending=False,ignore_index=True)
max_disc[["Product_Name",'discount']].head(10)


# ## Finding the mobile phones what all fall under price range 25000 to 30000

# In[28]:


sell_price =df[(df['selling_price']<30000) & (df['selling_price']>25000)]
result1=sell_price[["Product_Name",'selling_price']]
result1.head(10)


# ## Finding the phones which have 18 months warranty and rating greated than 4.5

# In[29]:


best_products=df[(df['warranty_in_months']==18) & (df['rating']>4.5)]
best_product=best_products[["Product_Name",'warranty_in_months']]
best_product


# In[30]:


best_products.plot.bar("Product_Name","warranty_in_months",color=(['b','c']),width=0.3)
font1={"color":"green"}
plt.ylabel('Warranty in Months',fontsize=16,fontdict=font1)
plt.xlabel('Phone',fontsize=14,fontdict=font1)
plt.grid()
plt.show()


# ### Finding the phones which comes under 24 months warranty

# In[31]:


best_products12=df[(df['warranty_in_months']==24) & (df['rating']>4)]
best_products12


# In[32]:


best_products12.Product_Name.unique()


# In[33]:


best_products12.Product_Name.nunique()


# #### there are total 7 phones which comes under 24 months warranty 

# In[34]:


best_product.count()


# ### there are total 26 phones which have 18 months warranty

# ## Top 10 phones for which maximum people have given the rating

# In[35]:


best_phone_by_rating=df[["Product_Name","rating_count"]].value_counts().reset_index().sort_values(["rating_count"],ascending=False,ignore_index=True)
x=best_phone_by_rating.head(10)
x


# In[36]:


x.plot.bar("Product_Name","rating_count",color=(['y','c']),width=0.3)
font1={"color":"black"}
font2={"color":"blue"}
plt.ylabel('Charges in Lakhs',fontsize=16,fontdict=font1)
plt.xlabel('region',fontsize=14,fontdict=font1)
plt.grid()
plt.show()


# ## Top 10 costly phones available

# In[37]:


top10=df.groupby(["Product_Name","selling_price"]).sum().reset_index().sort_values(['selling_price'],ascending=False,ignore_index=True)
top=top10.head(10)
top.head(10)


# In[38]:


result=top[["Product_Name","selling_price"]]
result


# In[39]:


result.plot.bar("Product_Name","selling_price",color=(['g','c']),width=0.3)
font1={"color":"Blue"}
plt.ylabel('Selling_price',fontsize=16,fontdict=font1)
plt.xlabel('Phone',fontsize=14,fontdict=font1)
plt.grid()
plt.show()


# In[40]:


df.to_csv("C:/Users/shahn/OneDrive/Desktop/Project_Flipkart_final400.csv")


# ## conclusion

# #### Scrapped flipcart website and then performed data cleaning, then impoted this data into jupyter notebook and performed exploratory data analysis (EDA), I have checked best phones on the basis of their price,discount,battery power, ram and rom.
