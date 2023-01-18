def sayhello(name):
    return f"Hola {name}, bienvenido al sistema."


if __name__ == "__main__":
    name = input("Introduzca su nombre: ")
    print(sayhello(name))

