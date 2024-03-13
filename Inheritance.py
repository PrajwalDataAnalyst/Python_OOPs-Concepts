#!/usr/bin/env python
# coding: utf-8

#                      Bank Account System: 
# Design a system to manage different types of bank accounts such as savings accounts, checking accounts, and investment accounts.
# Implement a base class Account with methods for deposit, withdrawal, and balance inquiry.
 Inheritance : - Inheritance is a core concept in object-oriented programming (OOP) that allows a new class to inherit properties and behavior
(attributes and methods) from an existing class. This enables code reuse, promotes modularity, and allows for the creation of hierarchies of classes.

                There are several types of inheritance:

Single Inheritance: In single inheritance, a class inherits properties and behavior from only one parent class. 
This is the simplest form of inheritance.

Multiple Inheritance: Multiple inheritance allows a class to inherit properties and behavior from multiple parent classes.
This enables the child class to have characteristics of multiple parent classes.

Multilevel Inheritance: In multilevel inheritance, a class inherits properties and behavior from a parent class,
and then another class inherits from this derived class. This forms a chain of inheritance.Multilevel Inheritance: 
In multilevel inheritance, a class inherits properties and behavior from a parent class, and then another class inherits from this derived class.
This forms a chain of inheritance.

Hierarchical Inheritance: Hierarchical inheritance involves multiple child classes inheriting from the same parent class. 
Each child class shares properties and behavior from the common parent class.

Hybrid Inheritance: Hybrid inheritance is a combination of multiple inheritance and hierarchical inheritance. 
It involves inheriting from multiple parent classes and forming a hierarchical structure.
# In[28]:


# example for Multilevel Inheritance 
import random
bank_names = [
    "Bank of America",
    "JPMorgan Chase Bank",
    "Wells Fargo Bank",
    "Citibank",
    "Goldman Sachs",
    "Morgan Stanley",
    "U.S. Bank",
    "TD Bank",
    "PNC Bank",
    "Capital One Bank"
]

class bank_info:
    def __init__(self,cust_name,account_num,deposit,withdraw):
        self.cust_name=cust_name
        self.account_num=account_num
        self.deposit=deposit
        self.withdraw=withdraw
class customer_details(bank_info):
    def desplay_cust_details(self):
        print( "customer : ",self.cust_name,"\n","account number : ",self.account_num,"\n","Bank name = ",random.choice(bank_names))
        n=int(input("if you want to withdraw :- YES OR 1 or NO FOR 2 \n"))
        if n==1:
            print("withdraw amount more than deposit \n")
            if self.deposit >=n:
                withdr=int(input("Enter the amount to withdraw \n"))
                sum=self.deposit-withdr
                print("Your withdraw = ",withdr,"\n")
                print("your Balance = ",sum,"\n","Date = ",datetime.today())
            else:
                print("sorry .....! ")
A=customer_details("prajwal",10201250,10000,5000)
A.desplay_cust_details()
        


# In[40]:


# example for Multiple Inheritance 
class car:
    def __init__ (self,car_colour,car_gear,car_speed):
        self.car_colour=car_colour
        self.car_gear=car_gear
        self.car_speed=car_speed
        print("car colour =",car_colour,"\n","car gear =",car_gear,"\n","car speed=",car_speed)
class car_details: 
    def __init__(self,car_capacity,car_seat):
        self.car_capacity=car_capacity
        self.car_seat=car_seat
        print("car capacity = ",car_capacity,"\n","car seat =",car_seat,"\n")
class print_details(car,car_details):
    def __init__(self,car_colour,car_gear,car_speed,car_capacity,car_seat):   
        car.__init__(self,car_colour,car_gear,car_speed)
        car_details.__init__(self,car_capacity,car_seat)
A = print_details("Red", "Manual", "80mph", 5, "Cloth") 

