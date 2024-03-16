#!/usr/bin/env python
# coding: utf-8

# In[3]:


from abc import ABC ,abstractmethod


# Abstraction in Python, as in any programming language, refers to the concept of hiding complex implementation details while providing
# a simple and easy-to-use interface. 
# It allows programmers to focus on the essential aspects of an object or system without being concerned about the internal complexities.

# In[21]:


class abstractmethod_1:
    @abstractmethod
    def shape(self):
        pass
class circel(abstractmethod_1):
    def __init__(self,a):
        self.a=a
    def shape(self):
        return 3.14*self.a*self.a
class rectangle(abstractmethod_1):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def shape(self):
        return self.a*self.b
sh=rectangle(10,20)
sh1=circel(20)
print("rectangle =",sh.shape())
print("circel =",sh1.shape())


# In[ ]:




