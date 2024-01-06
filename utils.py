def mostrarInfoBasica(diccionario, name):
        print(40 * "-")
        print("| ID \t| NOMBRE ")
        print(40 * "-")
        for llave, valor in diccionario.items():
            print(f"| {llave} \t| {valor[name]} ")
            print(40 * "-")