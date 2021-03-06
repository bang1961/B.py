# -*- coding: utf-8 -*-
"""notExercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ph1czLNJQfOYF-UaVdgPmZ-JdZTCTCpm
"""

!apt-get update
!apt-get install -y fonts-nanum
!fc-cache -fv
!rm ~/.cache/matplotlib -rf

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.unicode_minus']=False
plt.rc('font',family='NanumBarunGothic')

import warnings
warnings.filterwarnings('ignore')

!ls -l

import pandas as pd
DF=pd.read_excel('notExercise.xls')
DF.head()

DF.drop(columns='기간',inplace=True)
DF.tail()

DF['대분류'][23:]

DF.drop(index=range(23,53),inplace=True)
DF

DF_G =DF[DF['대분류']=='성별'].copy()
DF_G

DF_G.drop(columns='대분류',inplace=True)
DF_G

DF_G.set_index('분류',inplace=True)
DF_G

import matplotlib.pyplot as plt

figure, ax=plt.subplots(2,2,figsize=(10,10))

DF_G['운동을 할 충분한 시간이 없어서'].plot.pie(explode=[0,0.02],ax=ax[0][0],autopct='%1.1f%%')

ax[0][0].set_title('운동을 할 충분한 시간이 없어서')
ax[0][0].set_ylabel('')

DF_G['함께 운동을 할 사람이 없어서'].plot.pie(explode=[0,0.02],ax=ax[0][1],autopct='%1.1f%%')

ax[0][1].set_title('함께 운동을 할 사람이 없어서')
ax[0][1].set_ylabel('')

DF_G['운동을 싫어해서'].plot.pie(explode=[0,0.02],ax=ax[1][0],autopct='%1.1f%%')

ax[1][0].set_title('운동을 싫어해서')
ax[1][0].set_ylabel('')

DF_G['운동을 할 만한 장소가 없어서'].plot.pie(explode=[0,0.02],ax=ax[1][1],autopct='%1.1f%%')

ax[1][1].set_title('운동을 싫어해서')
ax[1][1].set_ylabel('')

plt.show()

