#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Question 9
n=int(input("Enter a number:"))
def firstDigit(n) : 
    while n >= 10:  
        n = n / 10; 
    return int(n) 
def lastDigit(n) : 
    return (n % 10)  
#print(firstDigit(n), end = " ")  
#print(lastDigit(n)) 
print(firstDigit(n)+lastDigit(n))


# In[ ]:




