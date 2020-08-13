#!/usr/bin/env python3
import sys
print("Please write the path to install Trumpy:")
print("Example : /home/user/Trumpy")
ruta=input()
variable='path= \''+ruta+'/distributed-computing-master/project/\''
ruta=ruta+'/distributed-computing-master/project/'
print(ruta)
sys.path.insert(0, ruta)

archivos=['collecting_data.py','storedb.py','data_process.py']

for i in archivos:
    contenido = open(i).read().splitlines()
    contenido.insert(0,str(variable))
    f = open(i, "r+")
    f.writelines("\n".join(contenido))

with open('cron.py',"w") as cron:
    cron.write('#!/usr/bin/env python3\n')
    cron.write('import os \n')
    for i in archivos:
        comando='("/usr/bin/python3 '+ruta+i+'")'
        cron.write('os.system'+comando +'\n')
    cron.close()


