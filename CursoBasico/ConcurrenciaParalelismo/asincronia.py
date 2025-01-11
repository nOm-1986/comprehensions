"""
Asincronismo:
Las Corrutinas y asyncio
    Una corrutina es una función qu epuede ser pausada y retomada más tarde.
    Async ---- Await
"""
import asyncio
import time
import random

async def process_data(data):
    print(f"Procesando {data} ....")
    await asyncio.sleep(4)
    print(f'{data} processed')
    return data * 2

async def process_other_data(n):
    print(f'Processing another thing {n} .....')
    time.sleep(random.randint(1,3))
    print(f'Processing another thing {n} ----- Done')

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')
    await process_other_data(1)
    await process_other_data(2)
    await process_other_data(3)

asyncio.run(main())