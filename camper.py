def mostraCampers(campers):
    for llave, valor in campers.items():
        print(f"ID: {llave} | NOMBRE: {valor['nombreC']}")