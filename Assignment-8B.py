#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

data = pd.read_excel('LoadDatainkW.xlsx')
data.head()
data.shape


# In[3]:


hour_1 = data.iloc[0:-1, 2]
hour_2 = data.iloc[1:, 2]
print(hour_1.shape)
print(hour_2.shape)


# In[5]:


hour_2 = hour_2.reset_index()
hour_2 = hour_2['Load (kW)']


# In[6]:


df = pd.concat([hour_1, hour_2], axis = 1)
df.shape


# In[7]:


df.columns = ['Hour_1', 'Hour_2']
df.head


# In[8]:


normalized_df = (df - df.mean()) / df.std()
normalized_df.head()


# In[9]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(normalized_df.Hour_1, normalized_df.Hour_2, test_size = 0.10, random_state = 42)


# In[10]:


m = 1 #Initial value of slope
c = -1 #Initial value of intercept
lr = 0.01 #Learning Rate
delta_m = 1 #Initialising Δm
delta_c = 1 #Initialising Δc
v_m = 0
v_c = 0
lam = 0.9
max_iters = 100 #Maximum number of iterations  
iters_count = 0 #Counting Iterations


def deriv(m_f, c_f, x, y, v1, v2):
  global lam
  m_deriv = -1 * (y - (m_f - lam * v1) * x - c_f + lam * v2) * x
  c_deriv = -1 * (y - (m_f - lam * v1) * x - c_f + lam * v2)
  return m_deriv, c_deriv  


while iters_count < max_iters:
  for i in range(x_train.shape[0]):
    delta_m, delta_c = deriv(m, c, x_train.iloc[i], y_train.iloc[i], v_m, v_c)
    v_m = lam * v_m - lr * delta_m
    v_c = lam * v_c - lr * delta_c
    m += v_m
    c += v_c
  iters_count += 1
  print(f"Iteration: {iters_count}\tValue of m: {m}, \tValue of c: {c}")


# In[11]:


print(f"\nThe local minima occurs at: {m}, {c}")


# In[12]:


import numpy as np

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)


# In[13]:


y_pred_train = []
for i in x_train:
  y_p_tr = (m * i) + c
  y_pred_train.append(y_p_tr)
y_pred_train = np.array(y_pred_train)


# In[14]:



y_pred_test = []
for i in x_test:
  y_p_te = (m * i) + c
  y_pred_test.append(y_p_te)
y_pred_test = np.array(y_pred_test)


# In[15]:



import math
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import mean_absolute_error


#Training Accuracies
mse = math.sqrt(mean_squared_error(y_train, y_pred_train)) 
print('Root mean square error', mse) 
mse = (mean_squared_error(y_train, y_pred_train)) 
print('Mean square error', mse) 
mae=mean_absolute_error(y_train, y_pred_train)
print('Mean absolute error', mae)


# In[16]:


#Testing Accuracies
mse = math.sqrt(mean_squared_error(y_test, y_pred_test)) 
print('Root mean square error', mse) 
mse = (mean_squared_error(y_test, y_pred_test)) 
print('Mean square error', mse) 
mae=mean_absolute_error(y_test, y_pred_test)
print('Mean absolute error', mae)


# In[17]:


dec_1st = []
dec_1st.append(df.iloc[-1, 1])
for hour in range(24):
  normalised_pred = (dec_1st[-1] - df.mean()) / df.std()
  pred_load = m * normalised_pred + c
  pred_load = (pred_load * df.std()) + df.mean()
  dec_1st.append(pred_load)


# In[18]:


hour = input("Enter an hour(0-23) of 1st December, 2018 to predict the load")
print(f"Predicted Load (kW) at {hour} hours on 1st December, 2018: {dec_1st[1 + int(hour)][0]}")


# In[ ]:



