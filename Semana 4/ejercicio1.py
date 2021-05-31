# conversion de cadenas de caracteres

'''
cadena = 'grupo_09'
lista = list(cadena)
print(lista)
'''

'''
cad = 'hola'
cad2 = 'adios'
num = 15
tupla1 = tuple(cad)
tuplaGeneral = tupla1,num,tuple(cad2)
print(tuplaGeneral)
'''

'''
cadena = 'hhola'
print(set(cadena))

cadena_num = '298345328883940'
print(set(cadena_num))

lista = list()
for x in range(len(cadena_num)):
    lista.append(int(cadena_num[x]))

print(set(lista))
'''

# conversión de listas

'''
lista = ['h','o','l','a',1,2,3,('1',2)]
try:
    cadena = ''.join(lista)
    print(cadena)
except:
    print('Error al concatenar variables not string')


lista2 = list()

lista_3 = lista.pop(len(lista)-1)
lista.append(lista_3[0])
lista.append(lista_3[1])

for x in lista:
    lista2.append(str(x))

cadena = ''.join(lista2)
print(cadena)
'''

'''
lista = ['h','o','l','a',123,[1,2],'Grupo_09']
print(lista)
tupla = tuple(lista)
print(tupla)
'''

'''
lista = ['h','o','o','l','a',1,2,3]
conjunto = set(lista)
print(conjunto)
conjunto.add(4)
conjunto.add(5)

print(conjunto)
'''

# conversión de tuplas

'''
tupla = 'h','o','l','a'
cadena = ''.join(tupla)
print(cadena)
'''

'''
tupla = ('hola',12345,'grupo')
lista = list(tupla)
print(lista)
'''

tupla = ('hola',1234,'grupo','hola','Hola')
conjunto = set(tupla)
conjunto.add(555)
print(conjunto)