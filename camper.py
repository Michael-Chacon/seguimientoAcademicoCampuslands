import os
from conexiones import guardar as actualizarJson
from validaciones import romperCiclo
from menus import telefono as menuTelefono

def guardar(campers):
    bandera1 = True
    while bandera1:
        os.system('clear')
        print('\n----- Registrar un aspirante -----\n')
        id = input('Ingrese el id: ')
        if id in campers:
            print(f"\n*** El aspirante {campers[id]['nombreC']} ya tiene asigando el id {id} ***\n")
        else:
            nombre = input('Nombre del aspirante: ')
            apellidos = input('Apellidos: ')
            direccion = input('Direccion: ')
            acudiente = input('Acudiente: ')
            estado = 'inscrito'
            celular = []
            fijo = []
            bandera = True
            while bandera:
                print(menuTelefono)
                opc = input(": ")
                numero = input('Ingrese el numero: ')
                if opc == '1':
                    celular.append(numero)
                elif opc == '2':
                    fijo.append(numero)
                bandera = romperCiclo('ingresar otro número') # Función para preguntar si seguir pidiendo numero o no.
            campers[id] = {'nombreC': nombre, 'apellidos': apellidos, 'direccion': direccion, 'acudiente': acudiente, 'estado': estado, 'telefono': {'celular': celular, 'fijo': fijo}}
            actualizarJson('campers', campers)
            os.system('clear')
        bandera1 = romperCiclo('agregar otro aspirante')
        os.system('clear')
def mostraCampers(campers):
    for llave, valor in campers.items():
        print(f"ID: {llave} | NOMBRE: {valor['nombreC']}")