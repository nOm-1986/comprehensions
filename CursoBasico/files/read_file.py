FILE_URL: str = "d:/Development/Python/Python/CursoBasico/files/caperucita.txt"
#Leer un archivo línea por línea
try:
    with open (FILE_URL, "r") as archivo1:
        for lineas in archivo1:
            print(lineas.strip())
            pass
    archivo1.close()
except Exception as e:
    print("Woops. Tenemos un problema: ", e)

#leer todas la líneas en una lista
try:
    with open (FILE_URL, "r") as archivo2:
        lineas = archivo2.readlines()
        print(lineas)
    archivo2.close()
    
except Exception as e:
    print("Woops. Tenemos un problema: ", e)
