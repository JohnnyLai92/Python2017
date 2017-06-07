import os
import re
import linecache

rootdir = "D:\Project\JOP\DSICJOP\Development\Source\JOP\JOP\src\java\dsic"
for parent, dirnames, filenames in os.walk(rootdir):
        #print("parent is : "+parent)
        for dirname in dirnames:
                break;
                #print("\tHas folder={0}".format(dirname))
        for filename in filenames:
                #程式路徑、程式行數 
                #print("\tHas file={0},{1}".format(filename,len(open(parent+"\\"+filename,'r',encoding  = 'UTF-8').readlines())))
                count=0
                count0=0
                with open(parent+"\\"+filename,'r',encoding  = 'UTF-8') as f:
                        aa=1
                        for line in f:
                                count+=1
                                match = re.search(r' for ', line)
                                if match:
                                        aa=0
                                        # 得到匹配結果
                                        #if(re.search(r'{', line)):
                                        #        print("{0},{1}".format(count,line))
                                #迴圈內是否還有'{'
                                if(re.search(r'{', line) and aa==0):
                                      count0+=1
                                      if(re.search(r'.refreshRecord', line)):
                                              print("{0},{1},{2}".format(count,parent+"\\"+filename,line))
                                #迴圈內是否還有'}'
                                if(re.search(r'}', line) and aa==0 and count0>0):
                                      count0-=1
                                      if(re.search(r'.refreshRecord', line)):
                                              print("{0},{1},{2}".format(count,parent+"\\"+filename,line))
                                if(re.search(r'}', line) and aa==0 and count0==0):
                                               aa=1
                                               #print("{0},{1}".format(count,line))
                 
