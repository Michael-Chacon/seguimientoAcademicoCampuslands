import os
# from notas import estudiantePruebaAdmision as promedio
from validaciones import romperCiclo
from conexiones import guardar as actualizarJson, conexion
from menus import telefono as menuTelefono

campers = conexion('campers')
def guardar():
    bandera1 = True
    while bandera1:
        os.system('clear')
        print('\n----- Registrar un aspirante -----\n')
        id = input('Ingrese el id: ')
        if id in campers:
            print(f"\n*** Error - el aspirante {campers[id]['nombreC']} ya tiene asigando el id {id} ***\n")
        else:
            nombre = input('Nombre del aspirante: ')
            apellidos = input('Apellidos: ')
            direccion = input('Direccion: ')
            acudiente = input('Acudiente: ')
            estado = 'inscrito'
            haveRuta = 'no'
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
            campers[id] = {'nombreC': nombre, 'apellidos': apellidos, 'direccion': direccion, 'acudiente': acudiente, 'estado': estado, 'telefono': {'celular': celular, 'fijo': fijo}, 'haveRuta': haveRuta}
            actualizarJson('campers', campers)
            os.system('clear')
        bandera1 = romperCiclo('agregar otro aspirante')
        os.system('clear')


def registrarAsigancionRuta(idCamper):
    campers[idCamper]['haveRuta'] = 'si'
    actualizarJson('campers', campers)

        
# def mostraCampers(campers):
#     for llave, valor in campers.items():
#         print(f"ID: {llave} | NOMBRE: {valor['nombreC']}")
        

# def mostrarNotasAspirante(campers):
#     print(40 * "-")
#     print("| ID \t| NOMBRE \t| TEORICO \t| PRACTICO \t| PROMEDIO")
#     print(40 * "-")
#     for llave, valor in campers.items():
#         notas = promedio(llave)
#         print(f"| {llave} \t| {valor['nombreC']} \t| {notas[0]} \t| {notas[1]} \t| {notas[2]}")
#         print(40 * "-")