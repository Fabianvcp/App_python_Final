# El modelo, conexion con la base de datos
import sqlite3
import re
from tkinter import messagebox


#decorador para manejar errores en las operaciones con la base de datos
def manejar_errores(func):
    def envoltura(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error: {e}")
            
    return envoltura

# Decorador para validar campos de entrada (producto y stock)
def validar_campos(func):
    def envoltura(self, *args, **kwargs):
        # Depuración: imprimir los argumentos recibidos
        # Controlar la cantidad de argumentos
        if len(args) == 3:  # Creando un nuevo producto
            producto, descripcion, stock = args[0], args[1], args[2]
            producto_id = None  # No hay ID en la creación
        elif len(args) == 4:  # Modificando un producto existente
            producto_id, producto, descripcion, stock = args[0], args[1], args[2], args[3]
        else:
            messagebox.showerror("Error", "Número de argumentos no válido.")
            return
        # Validar que el producto solo contenga caracteres alfanuméricos y que stock sea un número
        if re.match("^[a-zA-Z0-9 ]+$", str(producto)) and isinstance(stock, int):
            return func(self, *args, **kwargs)
        else:
            print(f"Validación fallida: {producto_id if producto_id else 'nuevo producto :'}, {producto}, {descripcion}, {stock}")  # Mensaje de depuración
            messagebox.showerror("Error", "El 'producto' solo debe contener caracteres alfanuméricos y 'stock' debe ser un número.")
    return envoltura



class Modelo:
    
    def __init__(self):
        self.crear_bd()
        self.observadores = []

    def agregar_observador(self, observador):
        """Agregar un observador a la lista."""
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador):
        """Eliminar un observador de la lista."""
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar_observadores(self):
        """Notificar a todos los observadores registrados."""
        for observador in self.observadores:
            observador.actualizar()    
        
    @manejar_errores
    def crear_bd(self):
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id INTEGER PRIMARY KEY,
                            producto TEXT NOT NULL,
                            descripcion TEXT NOT NULL,
                            stock INTEGER NOT NULL)''')
        conexion.commit()
        cursor.execute("PRAGMA table_info(productos)")
        columnas = cursor.fetchall()
        nombres_columnas = [columna[1] for columna in columnas]
        if "stock" not in nombres_columnas:
            cursor.execute("ALTER TABLE productos ADD COLUMN stock INTEGER NOT NULL DEFAULT 0")
            conexion.commit()
        conexion.close()
	
    @validar_campos
    @manejar_errores
    def agregar_producto(self, producto, descripcion, stock):
                conexion = sqlite3.connect("stock.db")
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO productos (producto, descripcion, stock) VALUES (?, ?, ?)",(producto, descripcion, int(stock)))
                conexion.commit()                
                conexion.close()
                print(f"Producto agregado: {producto}, {descripcion}, {stock}")  # Mensaje de depuración
                self.notificar_observadores()  # Notificar observadores tras agregar el producto


    @manejar_errores
    def buscar_producto(self, termino):
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE producto LIKE ? OR descripcion LIKE ?", (f'%{termino}%', f'%{termino}%'))
        productos = cursor.fetchall()
        conexion.close()
        return productos
    
    @manejar_errores                
    def obtener_productos(self):
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos

    @manejar_errores
    def borrar_producto(self, producto_id):
            conexion = sqlite3.connect("stock.db")
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
            conexion.commit()
            conexion.close()
            self.notificar_observadores()  # Notificar observadores tras borrar un producto
            
    @manejar_errores
    def vender_producto(self, producto_id, cantidad):
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        try:
            # Obtener el stock actual del producto
            cursor.execute("SELECT stock FROM productos WHERE id = ?", (producto_id,))
            stock_actual = cursor.fetchone()
            
            if stock_actual is None:
                raise ValueError("Producto no encontrado.")  # Si el producto no existe

            stock_actual = stock_actual[0]  # Obtener el valor del stock
            if stock_actual >= cantidad:
                total = stock_actual - cantidad
                cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (total, producto_id))
                conexion.commit()  # Asegúrate de hacer commit después de la actualización
                self.notificar_observadores()  # Notifica a los observadores después de vender un producto
            else:
                raise ValueError("No hay suficiente stock disponible.")
        finally:
            conexion.close()
            
    @validar_campos
    @manejar_errores
    def modificar_producto(self, producto_id, nuevo_producto, nueva_descripcion, nuevo_stock):
        print(f"Modificando producto ID: {producto_id}, nuevo_producto: {nuevo_producto}, nueva_descripcion: {nueva_descripcion}, nuevo_stock: {nuevo_stock}")
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET producto = ?, descripcion = ?, stock = ? WHERE id = ?", (nuevo_producto, nueva_descripcion, nuevo_stock, producto_id))
        conexion.commit()
        print("Cambios guardados en la base de datos.")
        conexion.close()
        self.notificar_observadores()  # Notifica a los observadores después de modificar un producto



