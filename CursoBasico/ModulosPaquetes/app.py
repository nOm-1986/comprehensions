# Si deseo importar todo el modulo utilizo import
import reports as r

# Si deseo solo utilizar una función especifica utilizo from
from reports import generate_expenses_report

# Generar reportes de vetnas y gastos usando funciones
sales_report = r.generate_sales_report('October', 10000)
expense_report = r.generate_expenses_report('December', 8000)
importacion_funcion = generate_expenses_report('January', 20000)

print(sales_report)
print(expense_report)
print(importacion_funcion)