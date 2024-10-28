"""Dictionary  Comprehension
    Iguales que los diccionarios, su inicialización se hace utilizando comprensión.
    Esto hace que el análisis sea fácil e interpretado a simple vista.
"""
import random

def run():

    countries = ['col','mex','bol','pe']
    #population = {}
    countri_dic = {country: random.randint(1,100) for country in countries}
    print(countri_dic)

    names = ['nico','fabo','maria','karen']
    ages = [15,17,35,36,85]

    information = {name:age for name,age in zip(names, ages)}
    print(information)

    var_a = {clave: valor for clave, valor in enumerate(range(0, 11))}
    #resultado = {0:0, 1:1, 2:2, 3:3, 4:4, ....}
    print(var_a)


def dictionary_with_condition():
    # countries = ['col','mex','bol','pe','ar','ve','ch','br','ec']
    # pupulation = [54, 63, 42, 36, 55, 10, 24, 100, 60]
    # more_population = {country: pop for country, pop in zip(countries, pupulation) if pop > 50}
    # less_population = {country: pop for country, pop in zip(countries, pupulation) if pop < 50}
    # print(more_population)
    # print(less_population)

    text = 'Hola, soy Fabián Beltrán'
    unique = {c: c.upper() for c in text if c in 'aeiou'}
    amount = {c: text.count(c) for c in text }
    amount2 = {c: text.count(c) for c in text if c in 'aeiouáéíóú'}
    #print(unique)
    print(amount)
    print(amount2)

if __name__ == '__main__':
    #run()
    dictionary_with_condition()
