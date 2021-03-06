# Author: Maria Carroll
# Extracting a URL

import re

#regex = '\w+='
#regex = '=\w+'
regex = '"((http)s?://.*?)"'
filename = r"C:\Users\maria\OneDrive\Desktop\Programming\pforcs-problem-sheet.py\pforcs-problem-sheet.py\tutorialdata\www1\access.log"
Output = []

with open(filename) as Logfile:
  for line in Logfile:
    Results = re.findall(regex,line)
    print(Results)





