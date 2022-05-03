import itertools

rut = reversed(input('Ingresa tu RUT sin puntos ni dígito verificador: '))
numeros = itertools.cycle((2, 3, 4, 5, 6, 7))
suma = 0

for digito, numero in zip(rut, numeros):
    suma += int(digito)*numero

resultado = 11 - suma % 11

if resultado == 10:
    dv = 'K'
elif resultado == 11:
    dv = 0
else:
    dv = resultado

print(f'Su dígito verificador es {dv}')
