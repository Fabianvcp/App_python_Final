# El modelo, conexion con la base de datos
import sqlite3
import re
from tkinter import messagebox

class Modelo:
    def __init__(self):
        self.crear_bd()

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

    def agregar_producto(self, producto, descripcion, stock):
        if re.match("^[a-zA-Z0-9 ]+$", producto) and str(stock).isdigit():
            try:
                conexion = sqlite3.connect("stock.db")
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO productos (producto, descripcion, stock) VALUES (?, ?, ?)",
                               (producto, descripcion, int(stock)))
                conexion.commit()
                print(f"Producto agregado: {producto}, {descripcion}, {stock}")  # Mensaje de depuración
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al agregar el producto: {e}")
            finally:
                conexion.close()
        else:
            messagebox.showerror("Error", "El 'producto' solo debe contener caracteres alfanuméricos y 'stock' debe ser un número.")

    def buscar_producto(self, termino):
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE producto LIKE ? OR descripcion LIKE ?", (f'%{termino}%', f'%{termino}%'))
        productos = cursor.fetchall()
        conexion.close()
        return productos

    def borrar_producto(self, producto_id):
        try:
            conexion = sqlite3.connect("stock.db")
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
            conexion.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al borrar el producto: {e}")
        finally:
            conexion.close()

    def vender_producto(self, producto_id, cantidad):
        try:
            conexion = sqlite3.connect("stock.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT stock FROM productos WHERE id = ?", (producto_id,))
            stock_actual = cursor.fetchone()[0]
            if stock_actual >= cantidad:
                cursor.execute("UPDATE productos SET stock = stock - ? WHERE id = ?", (cantidad, producto_id))
                conexion.commit()
            else:
                messagebox.showerror("Error", "No hay suficiente stock disponible.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al vender el producto: {e}")
        finally:
            conexion.close()

    def modificar_producto(self, producto_id, nuevo_producto, nueva_descripcion, nuevo_stock):
        if re.match("^[a-zA-Z0-9 ]+$", nuevo_producto) and str(nuevo_stock).isdigit():
            try:
                conexion = sqlite3.connect("stock.db")
                cursor = conexion.cursor()
                cursor.execute("UPDATE productos SET producto = ?, descripcion = ?, stock = ? WHERE id = ?",
                               (nuevo_producto, nueva_descripcion, nuevo_stock, producto_id))
                conexion.commit()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al modificar el producto: {e}")
            finally:
                conexion.close()
        else:
            messagebox.showerror("Error", "El 'producto' solo debe contener caracteres alfanuméricos y 'stock' debe ser un número.")

    def obtener_productos(self):
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos



