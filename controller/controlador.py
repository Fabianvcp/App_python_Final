from model.modelo import Modelo
from view.vista import Vista
from tkinter import messagebox

class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo  # Usar el modelo pasado como argumento
        self.vista = None

    def asignar_vista(self, vista):
        """Método para asignar la vista al controlador"""
        self.vista = vista
        self.modelo.agregar_observador(self.vista)

    def agregar_producto_interfaz(self):
        producto = self.vista.entrada_producto.get().strip()
        descripcion = self.vista.entrada_descripcion.get().strip()
        stock = self.vista.entrada_stock.get().strip()
        
        # Validar que los campos no estén vacíos y que el stock sea numérico
        if producto and descripcion and stock.isdigit():
            stock = int(stock)
            self.modelo.agregar_producto(producto, descripcion, stock)
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos con valores válidos.")

    def buscar_producto_interfaz(self):
        termino = self.vista.entrada_producto.get().strip()
        if termino:  # Validar que el término no esté vacío
            productos = self.modelo.buscar_producto(termino)
            self.vista.actualizar_lista(productos)
        else:
            messagebox.showerror("Error", "Por favor, ingresa un término de búsqueda.")

    def borrar_producto_interfaz(self):
        try:
            selected_item = self.vista.tree.selection()[0]
            producto_id = self.vista.tree.item(selected_item)['values'][0]
            self.modelo.borrar_producto(producto_id)
            self.actualizar_lista()
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un producto para borrar.")
            
    def vender_producto_interfaz(self):
        producto_id = self.vista.obtener_producto_seleccionado()
        if producto_id is None:
            messagebox.showerror("Error", "Por favor, selecciona un producto para vender.")
            return  # Muestra error si no hay producto seleccionado

        cantidad = self.vista.entrada_stock.get().strip()
        if not cantidad.isdigit():
            messagebox.showerror("Error", "Por favor, introduce una cantidad válida.")
            return

        cantidad = int(cantidad)  # Convertir a entero si es un número válido

        try:
            self.modelo.vender_producto(producto_id, cantidad)
            self.actualizar_lista()
        except ValueError:
            messagebox.showerror("Error", "Introduce un valor numérico válido para la cantidad.")
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un producto para vender.")

    def modificar_producto_interfaz(self):
        producto_id = self.vista.obtener_producto_seleccionado()
        if producto_id is None:
            messagebox.showerror("Error", "Por favor, selecciona un producto para modificar.")
            return  # Muestra error si no hay producto seleccionado
        
        try:   
            # Obtenemos los nuevos valores de los campos de entrada
            nuevo_producto = self.vista.entrada_producto.get().strip()  # Eliminar espacios en blanco
            nueva_descripcion = self.vista.entrada_descripcion.get().strip()
            nuevo_stock = self.vista.entrada_stock.get().strip()
            
            # Validar que el stock sea numérico
            if not nuevo_stock.isdigit():
                messagebox.showerror("Error", "El stock debe ser un número válido.")
                return
            
            # Convertir el stock a entero
            nuevo_stock = int(nuevo_stock)
            # Llamada al método del modelo para modificar el producto
            self.modelo.modificar_producto(producto_id, nuevo_producto, nueva_descripcion, nuevo_stock)
            # Actualizar la lista de productos
            self.actualizar_lista()

        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un producto para modificar.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores válidos.")

    def actualizar_lista(self):
        productos = self.modelo.obtener_productos()
        if self.vista:  # Asegurarse de que la vista esté asignada
            self.vista.actualizar_lista(productos)
        else:
            print("Vista no asignada")
            
    def obtener_productos(self):
        return self.modelo.obtener_productos()