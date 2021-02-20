# Author: Maria carroll
# Moby files

with open("moby.txt", "r+") as f:
    print("create a file")
    moby = f.read ()
f.close()

freq = moby.count("e")
print (freq)