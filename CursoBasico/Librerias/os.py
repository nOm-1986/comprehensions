import os
import platform as pl

#Listar archivos txt
#py_files = [f for f in os.listdir('../') if f.endswith('.py')]
py_files = [f for f in os.listdir('D:\\Development\\Python\\Python\\CursoBasico') if f.endswith('.py')]
#print("Archivos .py: ", py_files)

perfil_so = {
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_vuild',
    'system',
    'uname',
    'version',
}

for perfil in perfil_so:
    if hasattr(pl, perfil):
        print(f"{perfil} -> {getattr(pl, perfil)()}")