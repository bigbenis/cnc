import re
import os




f = open('2.txt', 'r')
name = str((f.readline())[5:-5]) + '.MPF'
yoba = f.readlines()
#print(yoba)
f = open('2.txt', 'w')
name = str((f.readline())[5:-5]) + '.MPF'
for line in yoba:
    if 'SUPA' not in line:
        f.write(line)
      
print(name)

f.close()
os.rename('2.txt', name)