# Author: Maria carroll
# Moby files 

# open moby text file to read adn then create the file 
with open("moby.txt", "r+") as f:
    print("create a file")
    moby = f.read ()
f.close()
# count the frequency of e,s that are in the moby document and print, result is 116960
freq = moby.count("e")
print (freq)
