#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##7
n=int(input("Enter any number"))
tot=0
while n>0:
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sun of digit:",tot)


# In[ ]:


##2

number_array=list()
number=int(input("Enter the numbers of elements you want"))
print("Enter numbers in array:")
for i in range(int(number)):
    n=input("number :")
    number_array.append(int(n))
print("ARRAY:",number_array)
print("Maximum value entered is :",max(number_array))
print("Minimum value entered is :",min(number_array))


# In[ ]:


##16

c=input("Enter a charecter")
print("The ASCII value of '"+ c +"'is",ord(c))


# In[19]:


##6

name_array=list()
name=chr(input("Enter five names you want"))
print("Enter names in array:")
for x in range(chr(name)):
    n=input("name :")
    name_array.append(chr(n))
print("ARRAY:",name_array)


# In[4]:


##18

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("enter base"))
exp=int(input("Enter exponential value:"))
print("result:",power(base,exp))


# In[5]:


##24

num=int(input("Choose a number:"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)


# In[10]:


##25

ch = input("Enter a charecter:")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch,"this is an alphabet")
else:
    print(ch,"this is a digit")


# In[13]:


##26

salary=int(input("Enter salary \n"))
if salary>=5000:
    print("the hra",(salary*15/100))
    print("the da",(salary*150/100))
else:
    print("the hra",(salary*10/100))
    print("the da",(salary*110/100))
    


# In[18]:


##20

fun=lambda x : x.replace("a","*")
print(fun("Ram has a bat"))


# In[ ]:


##8
x = input("enter the value: \n")
y = input("enter the value: \n")
temp=x
x=y
y=temp
print("the value of x is:".format (x))
print("the value of y is:".format (y))


# In[ ]:


>> "a" + "bc"


# In[ ]:


x = ['ab', 'cd']
for i in x:
i.upper()
print(x)


# In[ ]:




