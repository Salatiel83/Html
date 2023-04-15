def validar_numero_telefono(cadena):

    cadena = cadena.replace(" ", "").replace("-", "")

    if not cadena.isdigit():
        return False

    if len(cadena) != 10:
        return False

    return True

numero_telefono = input("Ingrese el n�mero de tel�fono (10 d�gitos): ")
if validar_numero_telefono(numero_telefono):
    print("El n�mero de tel�fono es v�lido.")
else:
    print("El n�mero de tel�fono no es v�lido.")
