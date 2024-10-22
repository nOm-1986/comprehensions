import statistics
import csv
FILE_URL: str = "d:/Development/Python/Python/CursoBasico/Statistics/monthly_sales.csv"
# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open(FILE_URL, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
#print(sales)

#Hallar la media
#mean_sales = statistics.mean(monthly_sales.values())
mean_sales = statistics.mean(sales)
print(f"La media es: ", mean_sales)

#Hallar la mediana
mean_sales = statistics.median(sales)
print(f"La mediana es: ", mean_sales)

#Hallar la moda
mean_sales = statistics.mode(sales)
print(f"La moda es: ", mean_sales)

#Hallar desviación Estándar
mean_sales = statistics.stdev(sales)
print(f"La desviacion estandar es: ", mean_sales)

#Hallar la varianza
mean_sales = statistics.variance(sales)
print(f"La varianza es: ", mean_sales)

max_sale = max(sales)
min_sale = min(sales)

range_sales = max_sale - min_sale
print(f"Rango de ventas: {range_sales}")