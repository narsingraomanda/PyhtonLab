# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:00:23 2019

@author: narsingaraom
"""
'''
fobj=open("clients.txt","w")
fobj.write("Python Programming")
fobj.write("scale language\n")
fobj.close()

##using context manager
with open(r"myfile.txt","w") as fobj:
    fobj.write("unix shell\n")
    '''
"""
with open("c:\\users\\admin\\Desktop\\myfile.txt","w") as fobj:
    fobj.write("unix Narsing\n")
    """
"""
try: 
    with open("demo.txt","r") as fobj:         
        for line in fobj:           
            line=line.strip()
            print(line)
except TypeError as error:
    print("Inavlid Operation")
    print("system error:",error)
except Exception as error:
    print("file not found...please check")
    print("system error:",error)
except FileNotFoundError as error:
    print("file not found...please check")
    print("system error:",error)

with open("annual-enterprise-survey-2018-financial-year-provisional-csv.csv","r") as fcsv:
    for line in fcsv:
        line=line.strip()
        ##print(line)
        listItems =line.split(',')
        print("street:"+listItems[0] +" "+"address:"+listItems[1])
        
"""

"""
import pandas as pd
csvfile="annual-enterprise-survey-2018-financial-year-provisional-csv.csv"
colnames=['Year','Industry_aggregation_NZSIOC']
df=pd.read_csv(csvfile,names=colnames)
##saved_column = df.column_name
print(df)
"""
"""
with open("annual-enterprise-survey-2018-financial-year-provisional-csv.csv","r") as fcsv:
    
    for rownum in range(sheet.nrows):
        
        x.append(sheet.cell(rownum, 7))
        """
'''
import csv
fobj=open("annual-enterprise-survey-2018-financial-year-provisional-csv.csv","r")
reader=csv.reader(fobj)
for line in reader:
    print(line)
    '''

###file in the list format###
    
'''
    fobjex=open("annual-enterprise-survey-2018-financial-year-provisional-csv.csv","r")
    print(fobjex.readlines()) #Whole file in list
    fobjex.close()
    '''

import os
ListofDirectories=os.listdir("c://")
for item in ListofDirectories:
    item=item.strip()
    print(item)
print("Difference")
cd=os.getcwd()
lstdir=os.listdir(cd)
for val in lstdir:
    val=val.strip()
    print(val)
print("count of files:\n")
print(len(lstdir))






    
    



    
