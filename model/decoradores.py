# decoradores.py
import sqlite3
import re
from tkinter import messagebox

def manejar_errores(func):
    """Decorador para manejar errores en las operaciones con la base de datos."""
    def envoltura(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error: {e}")
    return envoltura

def validar_campos(func):
    """Decorador para validar campos de entrada (producto y stock)."""
    def envoltura(self, *args, **kwargs):
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
            print(f"Validación fallida: {producto_id if producto_id else 'nuevo producto:'}, {producto}, {descripcion}, {stock}")
            messagebox.showerror("Error", "El 'producto' solo debe contener caracteres alfanuméricos y 'stock' debe ser un número.")
    return envoltura
