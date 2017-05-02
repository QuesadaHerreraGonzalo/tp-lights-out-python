def mostrarMenuDeInicio():
    print(" ☻ ☻ ☻ ¡¡Bienvenido a Lights Out!! ☻ ☻ ☻ ")
    modoElegido = input("¿Que modo desea jugar?  +Aleatorio+ (A), -Predeterminado- (P) o presione (X) para salir: ")

    print(modoElegido)

    modoElegido = modoElegido.lower()

    if (modoElegido == "a"):
        print("+¡Modo Aleatorio seleccionado!+")
    elif (modoElegido == "p"):
        print ("-¡Modo Predeterminado seleccionado!-")
    elif (modoElegido == "x"):
        print ("Selecciono salir :(")
