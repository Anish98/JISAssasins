#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 22

lists=[]
list1=[]
student=int(input("enter the no of students"))
for x in range(student):
    roll_no=int(input("enter the rollno"))
    lists.append(roll_no)
    stud_name=input("enter the name")
    lists.append(stud_name)
    marks1=int(input("enter the marks of the first subject"))
    list1.append(marks1)
    marks2=int(input("enter the marks of the 2nd subject"))
    list1.append(marks2)
    marks3=int(input("enter the marks of the 3rd subject"))
    list1.append(marks3)
    Total=0
    Average=0
    Total=marks1+marks2+marks3
    Average=Total/3
    print("the total marks of the student is ")
    print(Total)
    print("the average marks of the student")
    print(Average)
list1.sort(reverse=True)
print("the descending order of marks is :")
print(list1)
print("the names and roll no of students are:")
print(lists)


# In[ ]:




