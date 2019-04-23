# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:58:27 2019

@author: jjc姜金池
"""

import numpy as np

AH=#活塞面积
AL=#活塞面积
TH=#高温气缸温度
TL=#低温气缸温度
u=#与工质材质有关的参数
R=#飞轮半径
y_max=#配气活塞可以运动的最长距离
x_max=#工作活塞可以运动的最长距离
Cv=




def w(t):##飞轮的角速度################没有给定################
    
    
def theta(t):#飞轮转过角度与时间的关系
    return w(t)*t

def x(t):#工作活塞位移与时间的关系
    return R*(1+np.sin(theta(t)))

def y(t):#配气活塞位移与时间的关系
    return y_max/2*(1+np.cos(theta(t)))

def AH(t):
    return A0*(1+np.cos(theta(t)))

def AL(t):
    return A0*(1-np.cos(theta(t)))+A_max*x(t)/x_max

def T(t):
    return E(t)/Cv

def V(t):
    return Vc+Ap*x(t)

def P(t):
    return 2/5*E(t)/V(t)


def diff_E(t):###################E的导数，需要积分求出原函数##############
    return AH(t)*u*(TH-T(t))-AL(t)*u*(T(t)-TL)-(p(t)-p0)*Ap*R*w(t)*np.cos(theta(t))
    






    


    
