
# coding: utf-8

# In[3]:


#First python program on Jupyter Notebook
lst = ['a', 'b', 'c']
print(lst)


# In[9]:


#Program to find all numbers divisible by 7 but not multiple of 5 between 2000 and 3200 
output = []
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        output.append(str(i))

print (output)


# In[13]:


#Program to take first name and last name as inputs and print them in reverse order
FirstName = input("Input your First Name : ")
LastName = input("Input your Last Name : ")
print ("Hi  " + LastName + " " + FirstName)


# In[19]:


#Program to find the volume of a sphere with diameter as 12 cm
from math import pi
d = int(input("Enter diameter of a sphere: ")) # Taking input for diameter
r=d/2                                          # Calculating radius as 1/2 of diameter
v = (4/3) * pi * r**3                          # Calculating the volume of the sphere
print("Volume of a sphere with diameter " + str(d) + " is " + str(v)) # Output

