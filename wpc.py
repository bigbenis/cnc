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
    
    stringWPC = 'N5 G17\nN10 WORKPIECE(,"",,' + typeWpc + ',64,0,-' + height +',' + diam + ',' + diam +')'
    
    f = open('wpc.txt', 'r')
    yoba = f.readlines()
    f = open('wpc.txt', 'w')
    for line in yoba:
        if 'SUPA' not in line:
            f.write(re.sub(r'N10\s\S+', stringWPC, line))
    f.close()
    
elif typeWpc == '"BOX"':

    stringWPC = 'N5 G17\nN10 WORKPIECE(,"",,' + typeWpc + ',112,0,-3,3,0,0,100,200)'
    
    f = open('wpc.txt', 'r')
    yoba = f.readlines()
    f = open('wpc.txt', 'w')
    for line in yoba:
        if 'WORKPIECE' in line:
            f.write(re.sub(r'N10\s\S+', stringWPC, line))
    f.close()
    
else:

    stringWPC = 'N5 G17\nN10 WORKPIECE()'
    
#stringWPC - переменная, на которую нужно будет заменять найденную строку с заготовкой при записи

centerDrilling = 'MCALL CYCLE81(100,0,2,-0.5,,0,1,12) ' #цикл центровки

f = open('wpc.txt', 'r')
yoba = f.readlines()
f = open('wpc.txt', 'w')
for line in yoba:
    if 'SUPA' not in line:
        f.write(re.sub(r'\S+.MCALL.CYCLE82\S+', centerDrilling, line))
f.close()
