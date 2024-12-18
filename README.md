# Gestión de Stock

**Autores**: Ezequiel Tamargo y Fabián Alejandro Gallardo

## Descripción
InventarioApp es una aplicación de gestión de inventarios diseñada para almacenar, consultar, modificar y vender productos en stock. La aplicación está estructurada utilizando el patrón arquitectónico **Modelo-Vista-Controlador (MVC)**, lo que garantiza una separación clara entre la lógica de negocios, la interfaz de usuario y el control de flujo. Además, implementa el patrón **Observador** para notificar a la vista sobre cambios en el modelo, garantizando así la actualización automática de la interfaz cada vez que se realizan modificaciones en la base de datos.

## Características
- **Gestión de productos**: permite agregar, modificar, eliminar y vender productos con control de stock.
- **Interfaz gráfica (GUI)**: permite una experiencia interactiva y amigable con el usuario.
- **Validación de datos**: utiliza decoradores para validar entradas y manejar errores en la base de datos.
- **Patrón Observador**: mantiene sincronizada la vista al notificarla sobre cambios en el modelo.
  
## Requisitos
- **Python** 3.x
- **SQLite3** (base de datos)
- **Tkinter** (interfaz gráfica)

## Estructura del Proyecto
- `main.py`: Archivo principal que inicia la aplicación.
- `modelo.py`: Contiene la lógica de negocio y las operaciones de base de datos. Implementa el patrón Observador para la notificación de cambios.
- `controlador.py`: Conecta la lógica de negocio con la interfaz de usuario.
- `vista.py`: Define la interfaz gráfica de usuario (GUI) usando Tkinter.

## Instalación
1. Clona este repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd InventarioApp
    ```
2. Instala las dependencias necesarias (Tkinter viene instalado por defecto con Python en la mayoría de las plataformas).
3. Ejecuta el archivo `main.py` para iniciar la aplicación:
    ```bash
    python main.py
    ```

## Uso de la Aplicación
1. **Agregar Producto**: Ingresa el nombre, descripción y cantidad en stock de un producto para añadirlo a la base de datos.
2. **Buscar Producto**: Usa el campo de búsqueda para encontrar productos por nombre o descripción.
3. **Modificar Producto**: Selecciona un producto de la lista y edítalo según sea necesario.
4. **Eliminar Producto**: Selecciona un producto y elimínalo de la base de datos.
5. **Vender Producto**: Selecciona un producto e indica la cantidad a vender; el stock se actualizará automáticamente.

## Decoradores
El proyecto emplea decoradores para:
- **Manejo de Errores** (`manejar_errores`): captura excepciones y muestra mensajes de error cuando ocurre un problema de base de datos.
- **Validación de Campos** (`validar_campos`): valida que los campos `producto` y `stock` cumplan con los formatos esperados antes de realizar operaciones de base de datos.

## Funcionalidad del Patrón Observador
El patrón Observador permite a la **vista** (interfaz gráfica) suscribirse a cambios en el **modelo**. Cada vez que se actualiza la base de datos, el modelo notifica automáticamente a la vista, que actualiza la información mostrada sin necesidad de intervención manual.

## Ejemplo de Código (Modelo)
```python
class Modelo:
    
    def __init__(self):
        self.crear_bd()
        self.observadores = []

    def agregar_observador(self, observador):
        """Agrega un observador a la lista de suscriptores."""
        if observador not in self.observadores:
            self.observadores.append(observador)

    def notificar_observadores(self):
        """Notifica a todos los observadores registrados para actualizar la vista."""
        for observador in self.observadores:
            observador.actualizar()    
