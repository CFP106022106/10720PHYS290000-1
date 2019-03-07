#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt
x=np.random.random(100)
print(x)


# In[14]:


plt.hist(x,100)



# In[20]:


mu,sigma=0,0.1
s=np.random.normal(mu,sigma,100000)
plt.hist(s,1000)

plt.show()


# In[24]:


bins=np.linspace(-0.5,0.5,21,endpoint=True)
print(bins)
plt.hist(s,bins)
plt.show()


# In[49]:


import math
h=6.62*10**-34
c=3*10**8
k=1.38*10**-23
T=7000
num=1000
v=np.linspace(0,10**15,num)
B=2*h*v**3/c**2/(math.e**(h*v/k/T)-1)
plt.plot(v,B,".")
dB=np.random.normal(0.,10**-8.5,num)
B+=dB
plt.plot(v,B,'c.')

plt.show()


# In[ ]:




