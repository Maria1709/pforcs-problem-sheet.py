# Author:Maria Carroll
# Week 9 Session id
# https://www.programcreek.com/python/?CodeExample=get+session
# Lecturer Andrew Beatty

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# open file access.log
filename = "access.log"
# open file
try:
    file = open(filename, 'r', encoding='utf8')
except FileNotFoundError:
    print("The file " + filename + " was not found.")
    sys.exit(1)
colNames= colNames= ('ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dont know'
)
df = pd.read_csv(logFileName, sep=' ', header= None, names=colNames)

print(df)
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group()

# use regular expression to extract session id
regex = r'(?<==)\w*\s' 


