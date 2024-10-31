import datetime

class ObservadorConsola:
    def actualizar(self, accion, datos):
        """Método que se llama cuando se notifica un cambio."""
        ahora = datetime.datetime.now()
        print(f"[{ahora}] Datos actualizados: {accion} - {datos}")