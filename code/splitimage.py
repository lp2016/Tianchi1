# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:26:51 2017

@author: mfs
"""
#输入jpg，输出png，只需要修改输入输出路径即可


import os
from PIL import Image
import cv2
import numpy as np


#修改图片名称
def modify_name(path):
    image_name = os.listdir(path)
    for temp in image_name:
       print(temp)
       new_name = temp.split('k')[1]
       print(new_name)
 
       os.rename(path+temp,path+new_name)

#0,255 --> 0,1,同时三通道图片变成单通道
def to_0_1(path):
    for filename in os.listdir(path):              #listdir的参数是文件夹的路径
       print(filename)
       img1 = cv2.imread(path+filename,0)  
       img=img1 >128
       img1=np.multiply(img.astype(int),255)
    
       cv2.imwrite(path+filename, img1)


def splitimage(src, rownum, colnum, dstpath):
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]
        ext1 = 'png'
        print(ext)
        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext1))
                num = num + 1

        print('图片切割完毕，共生成 %s 张小图片。' % num)
    else:
        print('不合法的行列切割参数！')
        
        

if __name__=="__main__":
    input_path = 'F:\\tianchi\\train\\'
    output_path='F:\\tianchi\\result\\'
    num = 0
    for filename in os.listdir(input_path):
        src_new =input_path + filename
        print(src_new)   
        if os.path.isfile(src_new):
            if (output_path == '') or os.path.exists(output_path):
                #row = int(input('请输入切割行数：'))
                #col = int(input('请输入切割列数：'))
                row = 4
                col = 4
                if row > 0 and col > 0:
                    splitimage(src_new, row, col, output_path)
                else:
                    print('无效的行列切割参数！')
            else:
                print('图片输出目录 %s 不存在！' % output_path)
        else:
            print('图片文件 %s 不存在！' % src_new)
        num = num + 1    
        print('输出' + str(num) + '遍')

    


