# main.py
# Archivo principal: importa las clases, crea objetos y realiza pruebas.

from modelos import Contacto, Mensaje, MensajeCorreo, MensajeTexto


# Creamos contactos.
esdras = Contacto("Esdras", "esdras@ejemplo.com")
profesor = Contacto("Profesor", "profesor@ejemplo.com")

# Creamos mensajes de diferentes tipos.
mensaje_general = Mensaje(esdras, "Practica de modulos en Python")
correo = MensajeCorreo(
    esdras,
    "Entrega del Avance 3",
    profesor
)
sms = MensajeTexto(
    profesor,
    "La actividad ya esta disponible",
    "3312345678"
)

# Encapsulamiento: consultamos el asunto mediante un metodo.
print("ASUNTO ORIGINAL:", mensaje_general.get_asunto())

# Probamos el setter para modificar el asunto.
mensaje_general.set_asunto("Proyecto de programacion orientada a objetos")
print("ASUNTO ACTUALIZADO:", mensaje_general.get_asunto())

# Polimorfismo: todos los objetos responden a resumen(),
# pero cada tipo de mensaje muestra informacion diferente.
mensajes = [mensaje_general, correo, sms]

print("\nRESUMEN DE MENSAJES")
for mensaje in mensajes:
    print("-", mensaje.resumen())

# Composicion: accedemos al objeto Contacto contenido en Mensaje.
print("\nPRUEBA DE COMPOSICION")
print("Datos del remitente:", correo.remitente.mostrar_datos())

print("\nTodas las pruebas finalizaron correctamente.")
