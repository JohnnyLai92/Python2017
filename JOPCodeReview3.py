#計算程式支數
import os
import re 

rootdir = "D:\Project\JOP\DSICJOP\Development\Source\JOP\JOP\src\java\dsic"
count=0
for parent, dirnames, filenames in os.walk(rootdir):
        print("parent is : "+parent)
        for dirname in dirnames:
                continue
                print("\tHas folder={0}".format(dirname))
        for filename in filenames:
                #程式路徑、程式行數 
                print("\tHas file={0},{1}".format(filename,len(open(parent+"\\"+filename,'r',encoding  = 'UTF-8').readlines())))
                count+=1
print("程式總筆數 : "+str(count))
                 
                 
