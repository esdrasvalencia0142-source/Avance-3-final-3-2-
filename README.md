# Avance 3 Final: Composicion y Modulos

## Descripcion
Este proyecto continua el trabajo del Avance 2, cuyo ejemplo utilizaba la clase `Mensaje`.
Ahora se organiza el codigo en modulos y se aplican los principios de programacion orientada a objetos.

## Archivos
- `modelos.py`: contiene las clases `Contacto`, `Mensaje`, `MensajeCorreo` y `MensajeTexto`.
- `main.py`: importa las clases, crea objetos y ejecuta las pruebas.

## Conceptos aplicados
1. **Composicion:** cada objeto `Mensaje` contiene un objeto `Contacto` como remitente.
2. **Herencia:** `MensajeCorreo` y `MensajeTexto` heredan de `Mensaje`.
3. **Polimorfismo:** las subclases redefinen el metodo `resumen()` para mostrar informacion diferente.
4. **Encapsulamiento:** los atributos `__asunto`, `__nombre` y `__correo` son privados y se consultan mediante metodos.
5. **Modularizacion:** las clases estan en `modelos.py` y la ejecucion en `main.py`.

## Como ejecutar
Abre una terminal dentro de la carpeta del proyecto y ejecuta:

```bash
python main.py
```

## Estructura
```text
modulos-python/
|-- modelos.py
|-- main.py
|-- README.md
```
