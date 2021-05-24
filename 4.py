#import re
import os


f = open('1.txt', 'r')
name = str((f.readline())[5:-5]) + '.MPF'
f.close()

f = open('1.txt', 'r')
yoba = f.readlines()
f = open('1.txt', 'w')
for line in yoba:
    if 'SUPA' not in line:
        f.write(line)
      
print(name)

f.close()
os.rename('1.txt', name)