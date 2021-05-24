import re
import os

with open('2.txt', 'r') as pizda:
  yoba = pizda.readlines()
  name = pizda.readline()
  print(name)
with open('2.txt', 'w') as pizda:
  pizda.write(name)
  for line in yoba:
    if 'SUPA' not in line:
      pizda.write(line)
