#!/usr/bin/env python
# coding: utf-8

# Polymorphism allows for more flexibility and extensibility in your code, making it easier to add new classes that can be used interchangeably with existing classes without modifying the existing codebase. It is often associated with the following benefits:
# 
# 1) Code Reusability: Polymorphism allows the same code to be used with different objects, promoting code reuse and reducing redundancy.
# 
# 2) Flexibility: Polymorphic behavior allows for more flexible and dynamic interactions between objects, enhancing the adaptability of your code to different scenarios.
# 
# 3) Extensibility: Polymorphism facilitates the addition of new classes and behaviors to a system without affecting existing code, promoting scalability and maintainability.
# 
#                         There are two main types of polymorphism in Python:
# 
# 1] Compile-time polymorphism is achieved using method overloading and operator overloading.
# Method overloading allows defining multiple methods with the same name but different parameter lists. In Python, method overloading is simulated using default arguments or variable-length arguments (*args and **kwargs).
# Operator overloading allows defining the behavior of operators for user-defined classes.
# However, Python does not support true method overloading (as in languages like Java or C++) natively.
# Runtime Polymorphism (Dynamic Binding or Late Binding):
# 
# 2] Runtime polymorphism is achieved using method overriding.
# Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.
# It allows a subclass to provide its own implementation of a method that is already provided by its superclass, enabling different objects to respond to the same message (method call) in different ways.
# Method overriding is a key feature of inheritance and allows for dynamic dispatch, where the method to be called is determined at runtime based on the actual type of the object.
# This is the most common form of polymorphism used in Python and is achieved through inheritance and method overriding.

# In[49]:


#method overloading  (compile-time Polymorphism)
class method_overloading:
    def add(self,a,b):
        sum=a+b
        print("the addition of 2 numbers =",sum)
    def add(self,a,b,c=0):
        print("the addition of 3 numbers = ",a+b+c)
class method_overloading1(method_overloading):
    def sub(self,a,b):
        print("the substraction od 2 numbers =",a-b)
    def sub(self,a,b,c=0):
        
        s=a-b-c
        print("the substraction of 3 number =",s)
A=method_overloading1()
A.sub(10,20,30)
              
              


# In[65]:


#Method overriding (runtime Polymorphism)
class method_overloading:
    def father(self):
        print("i sleep 10 pm")
    def mother(self):
        print("i cook food around 8:30 pm")
class method_overrading1(method_overloading): 
    def father(self):
        super().father()
        print("i woke up morining 5 ")
    def mother(self):
        super().mother()
        print("i prepare breakfast around 8:30 am")
M=method_overrading1()
M.father()
M.mother()        


# In[74]:


#operator overloading
class operator_overloading:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self): 
        return self.a+self.b
    def __sub__(self):
        return self.a-self.b
    def __mul__(self):
        return self.a*self.b
    def __div__(self):   
        return self.a/self.b
O=operator_overloading(10,20)        
print(O.__add__())
print(O.__sub__())
print(O.__mul__())
print(O.__div__())

