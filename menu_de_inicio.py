def mostrarMenuDeInicio():
    print(" ☻ ☻ ☻ ¡¡Bienvenido a Lights Out!! ☻ ☻ ☻ ")
    modoElegido = input("¿Que modo desea jugar? " " +Aleatorio+ (A), -Predeterminado- (P) o presione (X) para salir: ")
    modoElegido = modoElegido.lower()

    if (modoElegido == "a"):
        print("+¡Modo Aleatorio seleccionado!+")
    elif (modoElegido == "p"):
        print ("-¡Modo Predeterminado seleccionado!-")
    elif (modoElegido == "x"):
        print ("Saliendo...  :(")
        exit()
    else:
        print("Por favor seleccione una de las teclas del menu o X para salir")
        mostrarMenuDeInicio()

