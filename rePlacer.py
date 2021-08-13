import re
import glob

#fileName = glob.glob('*.MPF')[0]

with open (glob.glob('*.MPF')[0],'r') as f: #глоб открывает любой файл с заданным расширением, нолик для отброса кавычек
	content = f.readlines()

with open (glob.glob('*.MPF')[0], 'w') as f:	
	for line in content:
		if 'WORKPIECE' in line: #если в строке есть заготовка, то
			wpc = line
			print(wpc)
			workpiece = re.search(r'(?:WORKPIECE)(\S+)', wpc) #ищем строку с заготовкой
			x = workpiece.group(1).split(',') #берем группу, где содержаться данные в скбоках и берем все данные, разделенные запятой

			typeWpc = str(x[3])
			wpcNew = 0

			if typeWpc == '"CYLINDER"':
				height = x[4]
				diam = x[8][0:-1]

				z = diam.split('.')
				z1 = str(z)
				z2 = z1.count("''")
				if z2 != 0:
					diam = diam[0:-1]
				else:
					diam = diam

				wpcNew = 'N5 G17\nN10 WORKPIECE(,"",,' + typeWpc + ',64,0,-' + height +',' + diam + ')\n'
				
				f.write(wpcNew)

		elif 'SUPA' not in line:
			f.write(line)
