import os
import re 

rootdir = "D:\Project\JOP\DSICJOP\Development\Source\JOP\DSIC.Flow\src\DSIC\FlowEngine"
for parent, dirnames, filenames in os.walk(rootdir):
        #print("parent is : "+parent)
        for dirname in dirnames:
                continue
                #print("\tHas folder={0}".format(dirname))
        for filename in filenames:
                #程式路徑、程式行數 
                #print("\tHas file={0},{1}".format(filename,len(open(parent+"\\"+filename,'r',encoding  = 'UTF-8').readlines())))
                count=0
                with open(parent+"\\"+filename,'r',encoding  = 'UTF-8') as f:
                        aa=1
                        for line in f:
                                count+=1
                                #搜尋SELECT(\s不管大小寫)及含'*'
                                if(re.search(r'/*(SELECT)\s', line) and re.search(r'\*', line)):
                                              print("{0},{1},{2}".format(count,parent+"\\"+filename,line)) 
                 
