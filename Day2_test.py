#!/usr/bin/env python
# coding: utf-8

# In[85]:


def add(*num):
    sm=sum(num)
    return sm
lst = [1,2,3,4]
print(add(*lst))


# In[154]:


string = 'PyThON'
rev_str=''
for i in string:
    if i ==i.lower():
        rev_str+=i.upper()
                
    else:
        rev_str += i.lower()
print(rev_str)
        
    


# In[153]:


lst = [4,1,2,1,2,4,]
for i in lst:
    if lst.count(i)>1:
        lst.remove(i)
        print(lst)
        


# In[145]:


lst = [2,3,4,1,2,1]
count = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            count =count+1
        if count>1:
            lst.remove(lst[i])
print(lst)
    


# In[121]:


lst.count(2)


# In[17]:


lst.insert(2,'Hi')


# In[18]:


lst


# In[19]:


b = lst.pop(2)
print(b)
print(lst)


# In[24]:


lst = [1,2,3,[1,2,3]]
for i in lst:
    if type(i) != 'list':
        print(type(i))
    else:
        print(end ='\t')
        for j in i:
            print(j)
        


# In[28]:


a= (1,2,3)
b =(1,2,3)


# In[43]:


x ={1,2,3,4}
y = {5,3,6,7}


# In[46]:


x.difference(y)


# In[55]:


x.add(5)


# In[48]:


frozenset([1,2,5,4,1])


# In[56]:


x


# In[57]:


a = {'name':'ali', 'college':'vit', 'branch': 'biomedical'}


# In[65]:


for i,j in a.items():
    print(i,j)


# In[73]:


a.update(branch='it', college='bit')


# In[71]:


a['branch'] = 'biomedical'


# In[74]:


a


# In[157]:


f ={
    'op':'equals',
    'rhs':'3',
    'lhs':{
        'op':'add',
        'rhs':{
            'op':'mul',
            'rhs':'21',
            'lhs':'x'
        },
        'lhs':'1'
    }
    
}


# In[170]:


type(f) is dict


# In[169]:


for i,j in f.items():
    if j is d.keys():
        print(True)
        break;
    
    


# In[171]:


def openup(j):
    for l,k in j.items():
        
for i,j in f.items():
    if dict == type(j):
        openup(j)


# In[84]:


type(f) == 'dict'


# In[97]:


n= int(input())
for i in range(n):
    add =0
    num = input()
    num1, num2 = num.split()
    num1 = num1[::-1]
    num2 = num2[::-1]
    add = str(int(num1)+int(num2))
    print(int(add[::-1]))


# In[99]:


def fact(num):
    while num!=0:
        return(num * fact(num-1))
n= int(input())
for i in range(n):
    mul = 1
    num = int(input())
fact(num)


# In[107]:


g = 'geeks'
g[::-1]


# In[109]:


f =[ele for ele in reversed(g)]


# In[155]:


d = {'equals': '=', 'add': '+', 'subtraction':'-', 'multiplication':'*','division':'/'}


# In[188]:


# your code goes here

n= int(input())
for i in range(n):
    add=0
    num = int(input())
    num %= 1000007
    for i in range(1,num+1):
        if i==1:
            add += 2
        else:
            add += ((i*2)+(i-1))
    print(add)


# In[194]:


n= int(input())
for i in range(n):
    add=0
    num = int(input())
    num %= 1000007
    add = (((3*(num**2))+ num)/2)
    print(int(add))


# In[215]:


def add_mul(num):
    add = 0
    mul = 1
    while(num>0):
        a = num%10
        num = num//10
        add += a
        mul *= a
    return (abs(mul-add))
        
num = int(input())
# print(num)
print(add_mul(num))


# In[213]:


-2%10


# In[218]:


73%5


# In[228]:


import math

num = int(input())
for i in range(num):
    n = int(input())
    if n>=38 and (n%5)>=3:
        print((n+(5-(n%5))))
    else:
        print(n)


# In[233]:


n = int(input("Enter the size of list: "))
k  = int(input('Search element please: '))
lst=[]
for i in range(n):
    lst.append(int(input()))
a = [i for i in range(len(lst)) if lst[i]==k]
print(*a)


# In[231]:


num = [1,2,3,5,4]
print(*num)


# In[ ]:




