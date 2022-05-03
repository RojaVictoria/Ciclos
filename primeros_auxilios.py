def main():
    while True:
        estimulos = input("¿La persona responde a estímulos? Responda si o no: ").lower()
        if estimulos not in ['no', 'si', 'sí']:
            print('Ingrese sí o no')
        elif estimulos == 'si' or estimulos == 'sí':
            print('Valorar la posibilidad de llevarlo al hospital más cercano')
            break
        elif estimulos == 'no':
            print('Abrir la vía aérea')

            respiracion = input("¿La persona está respirando? Responda si o no: ").lower()
            if respiracion not in ['no', 'si', 'sí']:
                print('Ingrese sí o no')
            elif respiracion == 'si' or respiracion == 'sí':
                print('Permitirle posición de suficiente ventilación')
                break
            elif respiracion == 'no':
                print('Administrar 5 ventilaciones y llamar a la Ambulancia')

                ambulancia = False
                while ambulancia is False or ambulancia == 'no':
                    signos_vitales = input("¿La persona tiene signos vitales? Responda si o no: ").lower()
                    if signos_vitales not in ['no', 'si', 'sí']:
                        print('Ingrese sí o no')
                    elif signos_vitales == 'si' or signos_vitales == 'sí':
                        print('Reevaluar a la espera de la ambulancia')
                        ambulancia = input("¿Llegó la ambulancia? Responda si o no: ").lower()
                        if ambulancia not in ['no', 'si', 'sí']:
                            print('Ingrese sí o no')
                        elif ambulancia == 'si' or ambulancia == 'sí':
                            print('Fin')
                    elif signos_vitales == 'no':
                        print('Administrar compresiones torácicas hasta que llegue la ambulancia')
                        ambulancia = input("¿Llegó la ambulancia? Responda si o no: ").lower()
                        if ambulancia not in ['no', 'si', 'sí']:
                            print('Ingrese sí o no')
                        elif ambulancia == 'si' or ambulancia == 'sí':
                            print('Fin')
                break


if __name__ == "__main__":
    main()
