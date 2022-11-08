#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Atm:
    def __init__(self):
        self.__pin ="" #for making it private for not hiding __Atm__pin
        self.__balance= 0
        print(id(self))
        self.menu()
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)== str:
            self.__pin = new_pin
            print("pin changed")
        else:
            print("pin not change")
        
    def menu(self):
        user_input = input(
                          "Hello ,how would you like to proceed?"
                         " 1- Enter 1 create pin"
                         " 2- Enter 2 to deposite"
                         " 3- Enter 3 to withdraw"
                         " 4- Enter 4 to check balance"
                          "5- Enter 5 to exit")
        if user_input == '1':
            print("Create pin")
            self.create_pin()
        elif user_input == '2':
            print("Deposite")
            self.deposite()
        elif user_input == '3':
            print("Withdraw")
            self.withdraw()
        elif user_input == '4':
            print("Check Balance")
            self.check_deposite()
        else:
            print("Exit")
    def create_pin(self):
        self.__pin = input("Enter your pin:")
        print("pin set successful")
    def deposite(self):
        temp = input("Enetr your pin")
        if temp == self.__pin:
            amount =int(input("Enter your amount"))
            self.balance =self.balance+amount
            print("Deposit successful")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount <self.balance:
                         self.balance =self.balance -amount
                         print("Success")
            else:
                         print("Insufficient funds")
                         
        else:
                         print("Insufficient funds")
    def check_deposite(self):
        temp =input("Enter ur pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
                         
            
sbi =Atm()
sbi.deposite()


# In[22]:


sbi.withdraw()
sbi.balance


# In[21]:


sbi.check_deposite()
sbi.balance


# In[2]:


Atm() 


# In[12]:


class Customer:
    def __init__(self,name,gender):
        self.name =name
        self.gender =gender
def greet(Customer):
    if Customer.gender =='Male':
        print("Hello",Customer.name,"Sir")
    else:
         print("Hello",Customer.name,"ma'am")
        
cust = Customer("Ankit","Female")

greet(cust)
        
        


# In[1]:


class Customer:
    def __init__(self,name,age,address):
        self.name =name
        self.age = age
        
    def intro(self):
        print("Iam ",self.name,"and Iam ",self.age)
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pin,new_state)
class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state
add = Address('Kolkata',700156,'WB')
cust = Customer('Neel','Male',add)
cust.edit_profile()  
c1
c1 =Customer("Nitin",34)
c2 =Customer("Ankit",45)
c3 =Customer("Zoya",32)

l = [c1,c2,c3]
for i in l:
    print(i.name)
        


# In[10]:


class Customer:
    def __init__(self,name,age,address):
        self.name =name
        self.age = age
        self.address = address
    def intro(self):
        print("Iam ",self.name,"and Iam ",self.age)
    
    def edit_profile(self,new_name=self.name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pin,new_state)
class Address:
    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
    def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state
add = Address('Kolkata',700156,'WB')
cust = Customer('Neel',34,add)

cust.edit_profile('Ankit','Gurgao',11236,'haryana')
print(cust.address.pincode)


# In[16]:


class User:
    def login(self):
        print("Login")
    def register(self):
        print("Register")
    def buy(self):
        print("Buying a phone")
class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")
    def buy(self):
        print("Buying a smartphone") #method overridding
stu1 =Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.register()
stu1.buy()


# In[17]:


class A :
    def __init__(self):
        self.var1=100
    
    def display1(self,var1):
        print("class A:",self.var1)
        
class B(A):
    def display2(self,var1):
        print("class B:",self.var1)
        
obj = B()
obj.display1(200)


# In[18]:


class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera =camera
        
class Smartphone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)# calling super within a constructor should be first statement
        self.os =os
        self.ram =ram
        print("Inside smartphone constructor")
s = Smartphone(9000,'samsung',12,'Android',2)
print(s.os)
print(s.brand)


# In[23]:


class Parent:
    def __init__(self,num):
        self.__num = num
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self,num,val):
        super().__init__(num)
        self.__val=val
    def get_val(self):
        return self.__val
son =Child(100,200)
print(son.get_num())
print(son.get_val())


# In[24]:


#Types of inheritance
class Product:
    def review(self):
        print("Product customer review")
class Phone(Product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a phone")
        
class Smartphone(Phone):
    pass

s = Smartphone(20000,'Apple',12)
p = Phone(1000,'Samsung',1)

s.buy()
s.review()
p.review()


# In[26]:


class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price  = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a phone")
        
class Product:
    def review(self):
        print("customer review")
    def buy(self):
        print("Buying a product")  
class SmartPhone(Phone,Product):
    pass

s = Smartphone(20000,'Apple',12)
s.buy()
s.review()


# In[ ]:


#method overloading

