import multiprocessing

def calculate_square(n):
    return n * n

if __name__ == "__main__":
    numbers = [x for x in range(1,40)]
    
    #Crear un pool
    with multiprocessing.Pool() as pool:
        results =  pool.map(calculate_square, numbers)

    print(f"Results: {results}")