#!/usr/bin/env python
# coding: utf-8

# Encapsulation in object-oriented programming involves bundling data and methods into a single unit (class), promoting data hiding and abstraction, 
# and providing controlled access through well-defined interfaces. 
# It enhances code modularity, maintainability, and security by enforcing information hiding and 
# reducing dependencies between different parts of a system.
# 
# 1) Getter methods  are provided to access the private attributes.2) 
# Setter methods) are provided to modify the private attributes.

# In[20]:


class College:
    def __init__(self, a, b):
        self.name = a
        self.__rollnum = b

    def get__rollnum(self):
        print(f"Hi, I am {self.name}\nMy roll number is {self.__rollnum}")

    def set__rollnum(self, x):
        self.__rollnum = x
        print(f"Hey, I am {self.name}\nMy roll number is modified to {x}")

C = College("Prajwal", 101)
print("accessing private method\n")
C.get__rollnum()
print("\n\nmodifying private method\n")

C.set__rollnum(105)


# In[ ]:




