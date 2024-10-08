# Gestión de Stock

Esta es una aplicación de escritorio para la gestión de productos y su stock, desarrollada en Python utilizando `tkinter` para la interfaz gráfica.

## Funcionalidades
- **Agregar Producto**: Permite añadir un nuevo producto con su descripción y cantidad de stock.
- **Buscar Producto**: Permite buscar un producto en el inventario.
- **Modificar Producto**: Modifica los detalles de un producto existente.
- **Borrar Producto**: Elimina un producto del inventario.
- **Vender Producto**: Descuenta una cantidad del stock del producto seleccionado.

## Validación de Datos
La validación de datos se realiza mediante un decorador, que verifica que el nombre del producto solo contenga caracteres alfanuméricos y que el stock sea un número.

### Decorador `validar_campos`
El decorador `validar_campos` se encarga de verificar que:
- El nombre del producto solo contiene caracteres alfanuméricos.
- El stock es un valor numérico entero.

### Ejecución del Proyecto
1. Clonar el repositorio.
2. Instalar las dependencias necesarias (si las hubiese).
3. Ejecutar el archivo principal con Python:
   ```bash
   python nombre_del_archivo.py
