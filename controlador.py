# La app se abre desde aca!
from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)
        self.actualizar_lista()

    def agregar_producto_interfaz(self):
        producto = self.vista.entrada_producto.get()
        descripcion = self.vista.entrada_descripcion.get()
        stock = self.vista.entrada_stock.get()
        self.modelo.agregar_producto(producto, descripcion, stock)
        self.actualizar_lista()

    def buscar_producto_interfaz(self):
        termino = self.vista.entrada_producto.get()
        productos = self.modelo.buscar_producto(termino)
        self.vista.actualizar_lista(productos)

    def borrar_producto_interfaz(self):
        selected_item = self.vista.tree.selection()[0]
        producto_id = self.vista.tree.item(selected_item)['values'][0]
        self.modelo.borrar_producto(producto_id)
        self.actualizar_lista()

    def vender_producto_interfaz(self):
        selected_item = self.vista.tree.selection()[0]
        producto_id = self.vista.tree.item(selected_item)['values'][0]
        cantidad = int(self.vista.entrada_stock.get())
        self.modelo.vender_producto(producto_id, cantidad)
        self.actualizar_lista()

    def modificar_producto_interfaz(self):
        selected_item = self.vista.tree.selection()[0]
        producto_id = self.vista.tree.item(selected_item)['values'][0]
        nuevo_producto = self.vista.entrada_producto.get()
        nueva_descripcion = self.vista.entrada_descripcion.get()
        nuevo_stock = int(self.vista.entrada_stock.get())
        self.modelo.modificar_producto(producto_id, nuevo_producto, nueva_descripcion, nuevo_stock)
        self.actualizar_lista()

    def actualizar_lista(self):
        productos = self.modelo.obtener_productos()
        self.vista.actualizar_lista(productos)

    def run(self):
        self.vista.mainloop()

if __name__ == "__main__":
    app = Controlador()
    app.run()

