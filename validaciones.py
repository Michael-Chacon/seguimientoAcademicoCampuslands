from conexiones import conexion
def existeElId(id, diccionario) -> bool:
    if id in diccionario:
        return True
    else:
        return False


def romperCiclo(mensaje):
    salir = input(f'Quiere agregar {mensaje}?\n\ts: Si\n\tn: No\n').lower()
    if salir == 'n':
        return False
    else:
        return True


def cuposEnHorario(idHorario):
    horarios = conexion('horarios')
    if horarios[idHorario]['disponible'] == 0: 
        return False
    else: 
        return True
