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


# In[ ]:


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

