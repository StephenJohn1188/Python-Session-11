#!/usr/bin/env python
# coding: utf-8

# # OOPS in Python

# In[10]:


class Student:
    #initialization Constructor --- to give values to data members
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    #Member Function
    def display(self):
        print("Name: ",self.name, "Grade: ",self.grade)


# In[6]:


#Create Object
stud1=Student("Jack", 9)
stud1.display()


# In[7]:


stud1.name


# In[8]:


stud1.grade


# In[9]:


stud2=Student("Andrew", 10)
stud2.display()


# In[11]:


class Student:
    #Class Variable
    Fees=8000
    #initialization Constructor --- to give values to data members
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    #Member Function
    def display(self):
        print("Name: ",self.name, "Grade: ",self.grade)


# In[12]:


stud1=Student("Jack", 9)
stud1.display()


# In[13]:


stud2=Student("Andrew", 10)
stud2.display()


# In[14]:


Student.Fees


# In[19]:


class Employee:
    def __init__(self,ID,Name, Dept):
        self.ID=ID
        self.Name=Name
        self.Dept=Dept
    def display(self):
        print("Name: ",self.Name , "ID: ",self.ID ,"Dept: ",self.Dept)

P1=Employee(1001, "Santhosh", "Human Resources")
P1.display()

P2=Employee(1002, "Prem", "Marketing")
P2.display()


# In[20]:


class Employee:
    def __init__(self,ID,Name, Dept):
        self.ID=ID
        self.Name=Name
        self.Dept=Dept
    def display(self):
        print("Name: ",self.Name , "ID: ",self.ID ,"Dept: ",self.Dept)


# In[22]:


def main():
    P1=Employee(1001, "Santhosh", "Human Resources")
    P1.display()


# In[24]:


#Calling the output in Development environment
if __name__=="__main__":
    main()


# In[30]:


class Employee:
    def __init__(self,ID,Name, Dept):
        print("Initialized method called")
        self.ID=ID
        self.Name=Name
        self.Dept=Dept
    def getdata(self, ID,Name,Dept):
        print("Get data method called")
        self.ID=ID
        self.Name=Name
        self.Dept=Dept
    def display(self):
        print("Hello","Name: ",self.Name , "ID: ",self.ID ,"Dept: ",self.Dept)
  
    def main():
        P1=Employee(1001, "Santhosh", "Human Resources")
        P1.display()
        
        P1.getdata(1001, "Santhosh", "Human Resources")


# In[32]:


if __name__=="__main__":
    main()

