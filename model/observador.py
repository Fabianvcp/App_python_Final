import datetime

class ObservadorConsola:
    def __init__(self, archivo_log="registro.txt"):
        self.archivo_log = archivo_log

    def actualizar(self, accion, datos):
        """Método que se llama cuando se notifica un cambio."""
        ahora = datetime.datetime.now()
        mensaje = f"[{ahora}] Datos actualizados: {accion} - {datos}\n"
        
        # Mostrar el mensaje en consola
        print(mensaje)
        
        # Guardar el mensaje en el archivo
        with open(self.archivo_log, "a") as archivo:
            archivo.write(mensaje)