import re
#import os


with open ('wpc.txt', 'r') as f:
    content = f.read()
    
workpiece = re.search(r'(?:WORKPIECE)(\S+)', content) # ищем то, что стоит после слова 'WORKPIECE'  

x = workpiece.group(1).split(',') #получим все данные, разделенные запятой

# тип заготовки
typeWpc = str(x[3])

if typeWpc == '"CYLINDER"':
    
    # высота заготовки
    height = x[4]

    # диаметр заготовки
    diam = x[8][0:-1]
    
    stringWPC = 'N5 G17\nN10 WORKPIECE(,””,,' + typeWpc + ',64,0,-' + height +',' + diam + '.' + diam +')'
    
elif typeWpc == '"BOX"':

    stringWPC = 'N5 G17\nN10 WORKPIECE(,””,,' + typeWpc + ',112,0,-3,3,0,0,100,200)'
    
else:

    stringWPC = 'N5 G17\nN10 WORKPIECE()'
    
#stringWPC - переменная, на которую нужно будет заменять найденную строку с заготовкой при записи

f = open('wpc.txt', 'r')
yoba = f.readlines()
f = open('wpc.txt', 'w')
for line in yoba:
    if 'SUPA' not in line:
        f.write(re.sub(r'N\S+', r'huy', line))

f.close()
