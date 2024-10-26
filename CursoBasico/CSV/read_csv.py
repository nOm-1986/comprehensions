import csv

#Leer un archvio
FILE_URL = "d:/Development/Python/Python/CursoBasico/CSV/products_updated.csv"
FILE_URL2 = "products_updated.csv"

"""
with open(FILE_URL, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
"""

#Mostrar la información por columnas
def imprimeInfo():
    with open(FILE_URL, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(f"Producto {row['name']}, precio: {row['price']}, cantidad {row['quantity']}, marca: {row['brand']}, categoria: {row['category']}")


def newProduct():
    new_product = {
        'name': 'Blue Yeti',
        'price': 199, 
        'quantity': 10, 
        'brand': 'ChargerMaster', 
        'category': 'Accessories', 
        'entry_date': '2024-02-05', 
        'total_value': '4800.0',
    }

    with open("CursoBasico/CSV/"+FILE_URL2, mode='a', newline="") as file:
        file.write("\n") # Para dar un salto al final 
        csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
        csv_writer.writerow(new_product)


def newCSV():

    with open("CursoBasico/CSV/"+FILE_URL2, mode='r') as file:
        csv_reader = csv.DictReader(file)
        #Obtener los nombres de las columnas existentes
        fieldnames = csv_reader.fieldnames + ['total_value'] + ['impuesto']

        with open("CursoBasico/CSV/products_updated_2.csv", mode='w', newline='') as updated_file:
            csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
            csv_writer.writeheader() #Escribir los encabezados.

            for row in csv_reader:
                row['total_value'] = float(row['price']) * int(row['quantity'])
                row['impuesto'] = 19.5
                csv_writer.writerow(row)
            


try:
    newCSV()
except Exception as e:
    print(f"Error tratando de: ", e)