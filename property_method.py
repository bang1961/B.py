#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Human:
    def __init__(self, age, name): ##초기화
        self.age = age   ##age값 초기화
        self.name = name ##name값 초기화

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다")


class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name) ##init 메서드가 두개이므로 overriding -> super()
        self.stunum = stunum

    def intro(self):
        super().intro()
        print("학번 : " + str(self.stunum))

    def study(self):
        print("하늘천 따지 검을현 누를황")


kim = Human(29, "김상형") ## kim= 메서드 삽입된 human
kim.intro() ## intro 메서드 실행

lee = Student(34, "이승우", 930011)
lee.intro()
lee.study()


# In[12]:


class Date:
    def __init__(self, month):
        self.month = month
    def getmonth(self):
        return self.month
    def setmonth(self, month): ##1~12면 setmonth 메서드
        if 1 <= month <= 12:
            self.month = month

today = Date(8)
today.setmonth(15)
print(today.getmonth())


# In[13]:


class Date:
    def __init__(self, month):
        self.inner_month = month
    def getmonth(self):
        return self.inner_month
    def setmonth(self, month):
        if 1<= month <= 12:
            self.inner_month = month
    month = property(getmonth, setmonth)

today = Date(8)
today.month = 15
print(today.month)


# In[17]:


class Test:

    def __init__(self):
        self.color = "red"

    def set_color(self,clr):
        self.color = clr

    def get_color(self):
        return self.color

if __name__ == '__main__':

    t = Test()
    t.set_color("blue")

    print(t.get_color())


# In[ ]:




