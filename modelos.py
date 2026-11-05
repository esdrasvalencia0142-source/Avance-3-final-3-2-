# modelos.py
# Clases del proyecto de Programacion Orientada a Objetos


# CLASE AUXILIAR: se utiliza para representar a una persona de contacto.
class Contacto:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def mostrar_datos(self):
        return f"{self.__nombre} ({self.__correo})"


# CLASE BASE: un Mensaje TIENE-UN Contacto como remitente.
class Mensaje:
    def __init__(self, remitente, asunto):
        self.remitente = remitente  # Composicion: objeto Contacto
        self.__asunto = asunto      # Encapsulamiento

    def get_asunto(self):
        return self.__asunto

    def set_asunto(self, nuevo_asunto):
        if nuevo_asunto.strip():
            self.__asunto = nuevo_asunto
        else:
            print("El asunto no puede estar vacio.")

    def resumen(self):
        return f"De {self.remitente.get_nombre()}: {self.__asunto}"


# SUBCLASE: hereda de Mensaje y agrega un destinatario.
class MensajeCorreo(Mensaje):
    def __init__(self, remitente, asunto, destinatario):
        super().__init__(remitente, asunto)
        self.destinatario = destinatario

    # Polimorfismo: redefine el metodo resumen().
    def resumen(self):
        return (
            f"Correo de {self.remitente.get_nombre()} "
            f"para {self.destinatario.get_nombre()}: {self.get_asunto()}"
        )


# SUBCLASE: hereda de Mensaje y agrega un numero de telefono.
class MensajeTexto(Mensaje):
    def __init__(self, remitente, asunto, telefono):
        super().__init__(remitente, asunto)
        self.telefono = telefono

    # Polimorfismo: misma operacion, comportamiento diferente.
    def resumen(self):
        return (
            f"SMS de {self.remitente.get_nombre()} "
            f"al numero {self.telefono}: {self.get_asunto()}"
        )
