import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Ejemplo de uso
longitud = 10
contrasena = generar_contrasena(longitud)
print(f"La contraseña aleatoria generada es: {contrasena}")
