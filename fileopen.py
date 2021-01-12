#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
count=0
secret = random.randint(1,100)
while True:
    num=int(input("숫자를 입력하세요(끝낼때 0):"))
    count+=1
    if num ==0:
        break
    if num == secret:
        print("맞췄습니다,%d번"%count)
    elif num > secret:
        print("입력한 숫자보다  더 작습니다")

    else:
        print("입력한 숫자보다 더큽니다")


# In[4]:


import sys
print(sys.version)
print(sys.platform)
if (sys.platform =="win32"):
    print(sys.getwindowsversion())
    
    


# In[5]:


import sys
print(sys.argv)


# In[7]:


str="89점"
try:
    score=int(str)
    print(score)
    a=str[5]
except ValueError as e:
    print(e)
    
except IndexError  as e:
    print(e)

print("작업완료")


# In[8]:


def calcsum(n):
    if (n<0):
        raise ValueError #강제
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum

try:
    print("-10=",calcsum(10))
    print("~-5=",calcsum(-5))

except ValueError:
    print('입력값이 잘못되었습니다.')


# In[9]:


open.a.txt()


# In[14]:


try:
    f=open("a.txt","rt")
    text= f.read()
    print(text)
except FileNotFoundError:
    print("No file...")
finally:
    f.close()


# In[15]:


f=open("a.txt","rt")
text=""
line=1
while True:
    row=f.readline()
    if not row:
        break
    text +=str(line)
    line +=1


# In[17]:


f=open("a.txt","rt")
rows=f.readlines()
for row in rows:
    print(row,end='')
f.close()


# In[ ]:




