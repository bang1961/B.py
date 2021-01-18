#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Date:
    def __init__(self, month):
        self.inner_month = month
    def getmonth(self):
        return self.inner_month
    def setmonth(self, month):
        if 1<= month <= 12:
            self.inner_month = month
    month = property(getmonth, setmonth)##property(get,set 메서드로만 month인수값 전달하는 접근제한방법)

today = Date(8)
today.month = 15
print(today.month)


# In[2]:


class Date:
    def __init__(self, month):
        self.inner_month = month
    @property
    def month(self):
        return self.inner_month
    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month

today = Date(8)
today.month = 15
print(today.month)


# In[3]:


class Car:
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)

pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()


# In[4]:


##staticmethod

class Car:
    @staticmethod
    def hello():
        print("오늘도 안전 운행 합시다.")
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)

Car.hello()


# In[5]:


class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

kim = Human(29, "김상형")
sang = Human(29, "김상형")
moon = Human(44, "문종민")
print(kim == sang)
print(kim == moon)
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)

kim = Human(29, "김상형")
print(kim)



# In[6]:


class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __len__(self):
        return self.age

kim = Human(29, "김상형")
print(len(kim))
from decimal import *

a = Decimal('1111111111')
b = Decimal('1111111111')

setcontext(BasicContext)
c = a * b
print(c)

setcontext(DefaultContext)
c = a * b
print(c)
from fractions import *

a = Fraction(1,3)
print(a)
b = Fraction(8, 14)
print(b)
from fractions import *

a = Fraction(2, 3)
b = Fraction(3, 5)
c = a + b
print(c)

d = c + 0.1
print(d)
import array

ar = array.array('i', [33, 44, 67, 89, 56])
for a in ar:
    print(a, end = ',')
ar.append(100)                  # 추가
del ar[0]                       	# 삭제
print("\nar[1] = ", ar[1])      		# 첨자 참조
print(ar[2:4])                  	# 슬라이스


# In[11]:


#모듈을 사용자에 저장 funny
import util


print("1inch=",util.INCH)
print("~10=",util.calcsum(10))


# In[14]:


import util2
print("~10=",util2.calcsum(10))
print("1inch=",util2.INCH)


# In[15]:


import sys
sys.path


# In[18]:


class Seq:
    def __init__(self,data):
        self.data=data
        self.index = -2
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index:self.index+2]
    
solarterm= Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k,end=',')


# In[ ]:




