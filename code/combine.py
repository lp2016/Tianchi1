# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:03:34 2017

@author: lip
"""

import os
import numpy as np
import cv2
"""
a = np.array([[1,7],[2,7],[3,7]])
b = np.array([[1,8],[2,8],[3,8]])
c = [[1],[2],[3]]
d = [[1],[2],[3]]
print(a)
print(b)
print(np.hstack((a,b)))     #拼接列
print(np.vstack((a,b)))     #拼接行

"""
#需要注意的一点，os.listdir(path)  不是按顺序列出目录下的所有文件，
#所以在进行拼接图片时注意如何拼接，不能按照os.listdir(path)返回的文件进行拼接


def combine_col():
    j=11
    foldersrc='F:\\tianchi\\combine\\mylabel2015\\{}\\'.format(j)
    T=cv2.imread('F:\\tianchi\\combine\\mylabel2015\\{}\\mask{}_0_960_.jpg'.format(j,j),0)
    for i in range(1,16):
        path='F:\\tianchi\\combine\\mylabel2015\\{}\\mask{}_'.format(j,j)+str(i)+'_960_.jpg'
        img=cv2.imread(path,0)
        T=np.hstack((T,img))
    print(T.shape)
    cv2.imwrite(foldersrc+'{}_result.png'.format(j),T)
    
def combine_row():
    foldersrc='F:\\tianchi\\combine\\mylabel2015\\result\\'
    T=cv2.imread('F:\\tianchi\\combine\\mylabel2015\\result\\8_result.png',0)
    for i in range(9,12):
        path='F:\\tianchi\\combine\\mylabel2015\\result\\{}_result.png'.format(i)
        img=cv2.imread(path,0)
        T=np.vstack((T,img))
    print(T.shape)
    cv2.imwrite(foldersrc+'2015_result.png',T)
combine_col()













