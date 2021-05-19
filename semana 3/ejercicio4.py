# x = x + 1

'''
n = 5
while n > 0:
    print(n)
    n = n - 1

print('Termino!')
'''

# retorno de la función es un entero
def factorial(n : int)-> int:
    resultado = 1
    n_actual = 2
    while n_actual <= n:
        resultado = resultado * n_actual
        n_actual += 1
    return resultado

print(factorial(0))
