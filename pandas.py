#Author: Maria carroll
#Ref:https://realpython.com/pandas-groupby/
#https://pandas.pydata.org/
# Lecture 10 Errors testing and logging 
# Lecturer: Andrew Beatty

import pandas as pd
import re 
import matplotlib.pyplot as plt
# filename = access log
fileName = 'access.log'

try:
    file = open(fileName, 'r') # opens file
    column names etc

    colNames= ('ip', 'time', 'url', 
           'status code', 'data response', 'referer', 'user agent', 'session id')

    # read in file
    df = pd.read_csv(file, sep=' ', header= None, names=colNames)
    # this will covert the time into the datetime format by removing the []
    df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
    df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
   # indexing datetime
    df = df.set_index(['time'])
# extracting the session id
    def extract_sessionid(x):
        wibble = re.search('(JSESSIONID=\S+)', x).group()
        id = re.split('=', wibble)[1]
        return id


df['sessionid'] = df['request'].apply(extract_sessionid)

print(df.groupby(by=['sessionid'])['size of response'].sum())

