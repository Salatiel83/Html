import re

def validar_correo(correo):

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(patron, correo):
        return True
    else:
        return False

correo_usuario = input("Ingresa un correo electr�nico: ")

if validar_correo(correo_usuario):
    print("El correo electr�nico es v�lido.")
else:
    print("El correo electr�nico no es v�lido.")
