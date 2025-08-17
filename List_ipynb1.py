#!/usr/bin/env python
# coding: utf-8

# # This is my List Notebook:-

# List are used to store multiple items in single variable,list is one of the 4 built in datatype in python used to store collection of data the other three are tuple,set and dictionary all with different qualuities and usage.list is created using square bracket[ ].

# ### List methods:-

# - List length
# - Change range of index 
# - Change list items
# - Insert
# - Append
# - Extend
# - Remove
# - Clear
# - Sort
# - Copy
# - Reverse
# - Join
#                                 
# 

# In[ ]:


#Assign a list to a variable my_list
my_list= [1,2,3,4,5]
print(my_list)


# In[3]:


thislist=["apple","banana","kiwi","mango"]
print(thislist)


# ###  list length:- 

# To determine how many function dose list have use len() function.

# In[4]:


my_list=["shaik","rabi","ahmed"]
print(len(my_list))


# In[5]:


thislist=[16,32,35,44,58,60,]
print(len(thislist))


# ###     List items and Datatypes:-

# List can be any datatype.
# Ex:- String,int,boolean,float.
# list1= ["apple","banana","kiwi"]
# list2= [1,2,3,4,5,]
# list3= [true,false,true]
# list4= [22.4,44.5,55.6]

# In[6]:


list1=["male",12,"true",10.5]


# ### type() :-

# From Python prespective lists are defined as objects with the datatype list.

# Ex:- What is the type of List ?

# In[7]:


thislist=["Apple","Banana","Cherry"]
print(type(thislist))


# ### Range of index:- 

# You can specify range of index by specifing where to start and where to end range.

# Ex:- Return second third and fourth item from list.
# 

# In[8]:


my_list = ["apple", "banana", "mango", "kiwi", "orange", "grapes"]
print(my_list[2:5])


# In[9]:


my_list = [10,20,30,40,60,70]
print(my_list[1:3])


# ### Change list items:-

# To change the value of the specific item refer the index number.

# Ex:- Change the second item

# In[10]:


thislist= ["apple","banana","cherry"]
thislist[1]="kiwi"
print(thislist)


# Ex:-Change the range of index

# In[11]:


thislist=["apple","banana","mango","orange","cherry"]
thislist[1:3]=["kiwi","melon"]
print(thislist)


# ### Insert Items:- 

# To insert a new item without replacing the existing value then use insert() method.

# Ex:- Insert melon at 2nd index

# In[12]:


my_list=["apple","banana","cherry"]
my_list.insert(2,"melon")
print(my_list)


# In[13]:


my_list=[10,23,40,44,56]
my_list.insert(4,100)
print(my_list)


# ### Append:- 

# To add any item at the end of the list use append() method. Append will take only 1 argument.

# Ex:-

# In[14]:


thislist = ["shaik","rabi"]
thislist.append("ahmed")
print(thislist)


# In[15]:


mylist = [10,23,43,52,66,88]
mylist.append(12)
print(mylist)


# ### Extend list:- 

# To append elements from another list to current list use the extend() method.

# Ex:- Add the elements of Tropical to thislist.

# In[16]:


thislist = [10,20,30,40]
tropical = [50,60,70]
thislist.extend(tropical)
print(thislist)


# In[17]:


thislist = ["shaik","rabi","ahemd"]
mydetails = [23,"completed Graduation"]
thislist.extend(mydetails)
print(thislist)


# ### Remove list items:- 

# Remove specified item, the remove() method remove the specified item from the list.

# In[18]:


thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)


# In[19]:


mylist =[12,24,56,76,34,55]
mylist.remove(56)
print(mylist)


# ### Remove specified Index:- 

# The pop() method removes the specified index.

# Ex:- Remove Second item.

# In[20]:


thislist = ["apple","banana","cherry","mango"]
thislist.pop(1)
print(thislist)


# Anothe key is del() same as pop.

# In[21]:


thislist = ["apple","banana","cherry","mango"]
del thislist[0]
print(thislist)


# Ex:- Remove last item.

# In[22]:


mylist = ["shaik","Rabi","ahmed"]
mylist.pop()
print(mylist)


# ### Clear the list:-

# To clear() method empties the list, the list still remains but it has no content.

# In[23]:


thislist = ["apple","banana","mango"]
thislist.clear()
print(thislist)


# In[24]:


mylist =[12,23,22,11,56]
thislist.clear()
print(thislist)


# ### Loop through a list:-

# You can loop through the list items by using a for loop.

# Ex:- Print all items in the list one by one.

# In[25]:


mylist = ["shaik", "rabi", "ahmed"]
for x in mylist:
    print(x)


# ### Loop through Index number:-

# You can also loop through the list item by refering to their index number, use the range() and len() to create a suitable iterator.

# Ex:- Print all the items referring to their index number

# In[26]:


mylist = ["apple", "banana", "cherry"]

for i in range(len(mylist)):
    print(mylist[i])


# In[27]:


thislist = [1,2,3,4,5,6]
for i in range(len(thislist)):
    print(thislist[i])


# ### Using a While loop:-

# You can loop through the list items by using a while loop, 
# Use the len() function to determine the length of the list start at 0 and loop your way through the list items by referring their index,
# Remember to increase the index by 1 after each iteration.

# Ex:- print all items using a while loop to go through all the index numbers.

# In[28]:


mylist = ["shaik", "rabi", "ahmed"]
i = 0
while i<len(mylist):
    print(mylist[i])
    i = i+1


# Ex:- int example

# In[29]:


thislist = [10,20,30,40,50]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# ### Sort list Alphanumerically 

# List objects have a sort() method to arrange a list in ascending order.

# Ex:-

# In[36]:


mylist = ["orange", "banana","apple","kiwi"]
mylist.sort()
print(mylist)


# Ex:-

# In[37]:


thislist = [50,40,30,20,10]
thislist.sort()
print(thislist)


# ### Sort list in decending:-

# In[43]:


mylist = [90, 50, 23, 55, 68]
mylist.sort(reverse = True)
print(mylist)


# In[44]:


thislist = ["apple", "banana", "kiwi", "melon"]
thislist.sort(reverse = True)
print(thislist)


# ### Copy Method:-

# You can use built in list method copy() to copy a list.

# Ex:- Make a copy of list with copy method.

# In[45]:


thislist = ["shaik", "rabi", "ahmed"]
thislist.copy()
print(thislist)


# In[46]:


mylist = [10,20,30,40,50]
mylist.copy()
print(mylist)


# ### Reverse the order of list items 

# In[47]:


thislist = ["shaik", "rabi", "ahmed"]
thislist.reverse()
print(thislist)


# In[48]:


mylist = [10,20,30,40,50]
mylist.reverse()
print(mylist)


# ### Join two lists:- 

# There are several ways to join or concatinate the list but the easiest way is + operator

# In[51]:


list1 = ["a", "b", "c"]
list2 = [1, 2, 3,]
list3 = list1 + list2
print(list3)


# --- Append  list will also do the same thing as join list.

# In[58]:


list1 = ["apple", "banana", "cherry"]
list2 = [10, 20, 30]
for x in list2:
 list1.append(x)
print(list1)

