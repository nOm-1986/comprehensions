def my_print(text: str):
    print(f'{text} ' * 2)

my_print('Un nuevo texto')
my_print('Hola mundo ' * 2)

a, b = 10, 12
c = a + b

def suma(num1: int, num2: int):
    print(num1 + num2)


def sum_with_range(min: int, max:int)->int:
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


print(sum_with_range(1,10))


def find_volum(length : int, width: int = 2, depth: int = 1)->list:
    return list((length * width * depth, width, 'hola'))
    #return [length * width * depth, width, 'hola']


def find_area(base: int, hight:int = 1):
    return {base * hight, }


resulta = find_volum(2)
area = find_area(3)

print(resulta)
print(f'Typo de retorno de find_volum: {type(resulta)}')
print(area)