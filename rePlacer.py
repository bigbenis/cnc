with open('1.txt', 'r') as pizda:
  yoba = pizda.readlines()
with open('1.txt', 'w') as pizda:
  for line in yoba:
    if 'SUPA' not in line:
      pizda.write(line)
