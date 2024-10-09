# Las matrices son mutables

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Tuplas - Son inmutables, por tal razón son muy rapidas para consultas y demás.
numbers = (1,2,3,4,5,6)
otraForma = 2,34,5,6,7,7
print(type(numbers))
print(type(otraForma))