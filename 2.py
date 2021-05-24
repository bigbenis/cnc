import re
import os
name = 0
with open('2.txt', 'r') as pizda:
  yoba = pizda.readlines()
with open('2.txt', 'w') as pizda:
  for line in yoba:
      name = re.findall(r'd\d\w+', line)
      pizda.write(line)
      #print(line)

      #
      #print(name)
print(str(name))
#(CYCLE83)(\([^()]*\)) - поиск скобок после цикла, выходит 2 группы
name = str(name)
#name = name[2:-2]
newname = str(name) + ".txt"

print(newname)

#os.rename("2.txt", newname)
