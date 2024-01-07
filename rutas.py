from conexiones import conexion

def retornarIdSala(idRuta):
    rutas = conexion('rutas')
    return rutas[idRuta]['idSalaR']