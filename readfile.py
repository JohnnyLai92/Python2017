import re
import os

count=0
count0=0
with open('f:\DBUtility.java','r',encoding  = 'UTF-8') as f:
        aa=1
        for line in f:
                count+=1
                match = re.search(r'while', line)
                if match:
                        aa=0
                        # 得到匹配結果
                        if(re.search(r'{', line)):
                                print("{0},{1}".format(count,line))
                #迴圈內是否還有'{'
                if(re.search(r'{', line) and aa==0):
                      count0+=1
                      if(re.search(r'.refreshRecord', line)):
                              print("{0},{1}".format(count,line))
                #迴圈內是否還有'}'
                if(re.search(r'}', line) and aa==0 and count0>0):
                      count0-=1
                      if(re.search(r'.refreshRecord', line)):
                              print("{0},{1}".format(count,line))
                if(re.search(r'}', line) and aa==0 and count0==0):
                               aa=1
                               print("{0},{1}".format(count,line))
                         
                #if(line.find("public") == 0 or line.find("public") == 4):
                #   print(line.replace("{","").lstrip(),end='')
                #print(len(open('f:\DBUtility.java','r',encoding  = 'UTF-8').readlines())) 
