import re
import os

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

with open ('0.000.000_not_modified.MPF') as reader:
    content = reader.readlines()

with open ('0.000.000_modified.MPF', 'w') as writer:
    for line in content:
        if 'SUPA' in line:
            writer.write(';SUPA WAS REMOVED\n')
        elif 'N140 D1' or 'Z2.' or 'Z-1.555' or 'F666' or 'F1337' or 'Z.445' in line:
            old_line = line
            new_line = multiple_replace(old_line, replace_values)
            writer.write(new_line)
        else:
            writer.write(line)
