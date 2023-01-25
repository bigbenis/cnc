import re
import os

listG0 = []

m09frame = 0

def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str

var_R3 = 'N141 R3=-0.15 ;PERVOE VREZANIE\n'
var_R10 = 'N142 R10=0.1  ;PRIRASCHENIE Z\n'
var_R20 = 'N143 R20=30   ;PODACHA Z\n'
var_R30 = 'N144 R30=80   ;PODACHA XY\n'
var_R35 = 'N145 R35=1    ;OTXOD Z (NA PODACHE)\n'
var_R40 = 'N146 R40=2    ;OTXOD Z (BYSTROE)\n'
r_variables = 'N140 D1\n\n'+var_R3+var_R10+var_R20+var_R30+var_R35+var_R40

replace_values = {
                  
                  "N140 D1": r_variables,
                  "Z2.": "Z=R40",
                  "Z-1.555": "Z=R3",
                  "F666": "F=R20",
                  "F1337": "F=R30",
                  "Z.445": "Z=R35",
                  
                  }

with open ('0.000.000_not_modified.MPF') as reader: # открываем программу для чтения
    content = reader.readlines() #читаем каждую строчку

    for line in content: # цикл перебора каждой строки программы
        matchM09 = re.search(r'(^N)(\d+)(\sM09)',line) # ищем строчку с М09
        if matchM09:
            m09frame = int(matchM09.group(2)) # берем из строки с М09 циферную часть и сразу делаем это интом

        matchG0 = re.match(r'(^N)(\d+)(\s)(G0)', line) # ищем строки с G0 с ловлей групп
        if matchG0:
            listG0.append(matchG0.group(2)) #добавляем в лист сразу номер кадра без "N"

gotobLine = 'N' + str(m09frame-2) + ' R3=R3-R10\n' + 'N' + str(m09frame-1) + ' IF R3>=-0.5 GOTOB ' + listG0[0] + '\n'   #полная фраза условия повторения цикла гравировки 

with open ('0.000.000_modified.MPF', 'w') as writer:
    for line in content:
        
        if 'SUPA' in line: #замена строк, где используется "SUPA"
            writer.write(';SUPA WAS REMOVED\n')

        elif 'M09' in line: #если в строке есть "М09" - добавляем условие повторения цикла гравировки
            writer.write(gotobLine)
            writer.write(line)

        elif 'WORKPIECE' in line: #если в строке определяется заготовка, надо добавить перед ней строку с "G17" для адекватной работы графики
            writer.write('N5 G17\n')
            writer.write(line)
            
        elif 'G17' in line:
            oldLine = line
            newLine = oldLine.split(' ')
            writer.write(newLine[0]+' '+newLine[1]+' '+newLine[3]+' '+newLine[4])

        elif ';-------------------------------------' in line:
            writer.write(line)
            writer.write('; -- PROGRAMMA ZARYAZHENA NA VODKU BABU GARMON I LOSOS\n\n')

        elif 'N140 D1' or 'Z2.' or 'Z-1.555' or 'F666' or 'F1337' or 'Z.445' in line:
            old_line = line
            new_line = multiple_replace(old_line, replace_values)
            writer.write(new_line)      
        else:
            writer.write(line)
