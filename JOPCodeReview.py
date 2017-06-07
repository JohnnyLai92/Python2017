import os
import re 

rootdir = "D:\Project\JOP\DSICJOP\Development\Source\JOP\JOP\src\java\dsic"
for parent, dirnames, filenames in os.walk(rootdir):
        #print("parent is : "+parent)
        for dirname in dirnames:
                continue
                print("\tHas folder={0}".format(dirname))
        for filename in filenames:
                #程式路徑、程式行數 
                #print("\tHas file={0},{1}".format(filename,len(open(parent+"\\"+filename,'r',encoding  = 'UTF-8').readlines())))
                count=0
                count0=0
                with open(parent+"\\"+filename,'r',encoding  = 'UTF-8') as f:
                        aa=1
                        for line in f:
                                count+=1
                                #要搜尋的字串開頭
                                if(re.search(r' while ', line)):
                                        aa=0 
                                #迴圈內是否還有'{'
                                if(re.search(r'{', line) and aa==0):
                                      count0+=1 
                                #迴圈內是否還有'}'
                                if(re.search(r'}', line) and aa==0 and count0>0):
                                      count0-=1
                                #顯示行數、程式路徑檔名、錯誤內容(refreshRecord)
                                if(re.search(r'.refreshRecord', line) and aa==0): 
                                        print("{0},{1},{2}".format(count,parent+"\\"+filename,line))
                                #搜尋到結尾
                                if(re.search(r'}', line) and aa==0 and count0==0):
                                               aa=1
                                               #print("{0},{1}".format(count,line))
                 
