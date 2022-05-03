from string import ascii_lowercase

password = str(input('Ingrese la contraseña: ')).lower()
letras = ascii_lowercase
intentos = 0

for caracter in password:
    for letra in letras:
        if caracter == letra:
            intentos += 1
            break
        else:
            intentos += 1

print(f'La contraseña fue forzada en {intentos} intentos')
