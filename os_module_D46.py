#Day 46

#OS module in python

import os

if(not os.path.exists("newfolder")):
    os.mkdir("newfolder") # it will create a new folder in the current directory.

for i in range (0,100):
    # os.mkdir(f"newfolder/Day{i+1}")
    os.rename(f"newfolder/Day{i+1}", f"newfolder/Day{i+1}_python") # it will rename the folder name.
    
import os

folders = os.listdir("newfolder") # it will give the list of all the folders in the current directory.

for folder in folders:
    print(folder)
    print(os.listdir(f"newfolder/{folder}"))

os.getcwd()