Cars Dataset

# ###  Instruction (for data cleaning)
# ### 1. Find all the null value in the dataset. If there is any null value in any column, then fill it with the mean of that column

# In[1]:
import pandas as pd

# In[2]:
car = pd.read_csv(r"E:\Car dataset for project python pandas.csv")

# In[4]:
car.head()

# In[5]:
car.shape

# In[42]:
car.isnull().sum()

# In[43]:
car['Cylinders'].fillna(car['Cylinders'].ffill(), inplace = True)


# ## Q2. Check what are the different types of Make in our Dataset. And, What is the count (occurance) of each Make in the data?
# In[44]:
car.head(2)

# In[45]:
car['Make'].value_counts()

# ## Q3.  Show all the records where Origin is Asia or Europe.
# In[46]:
car.head(2)

# In[48]:
car[car['Origin'].isin(['Asia' , 'Europe'])]

# ## Q4. Remove all the records (rows) where weight is above 4000
# In[49]:
car.head(2)
# In[50]:
car[car['Weight'] > 4000]

# In[51]:
car[~(car['Weight'] > 4000)]

# ## Q5. Increase all the values of "MPG_City by 3
# In[52]:

car.head()

# In[53]:
car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)

# In[54]:
car

