# Todo lo relacionado a la Vista
import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Stock")
        self.ventana.geometry("800x600")
        self.crear_interfaz()

    def crear_interfaz(self):
        frame_principal = tk.Frame(self.ventana, bg="#f0f0f0", padx=10, pady=10)
        frame_principal.pack(fill="both", expand=True)
        
        tk.Label(frame_principal, text="Producto:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_producto = tk.Entry(frame_principal)
        self.entrada_producto.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_principal, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entrada_descripcion = tk.Entry(frame_principal)
        self.entrada_descripcion.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_principal, text="Stock:").grid(row=2, column=0, padx=5, pady=5)
        self.entrada_stock = tk.Entry(frame_principal)
        self.entrada_stock.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Button(frame_principal, text="Agregar Producto", command=self.controlador.agregar_producto_interfaz).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(frame_principal, text="Buscar Producto", command=self.controlador.buscar_producto_interfaz).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(frame_principal, text="Borrar Producto", command=self.controlador.borrar_producto_interfaz).grid(row=3, column=3, padx=5, pady=5)
        tk.Button(frame_principal, text="Vender Producto", command=self.controlador.vender_producto_interfaz).grid(row=3, column=4, padx=5, pady=5)
        tk.Button(frame_principal, text="Modificar Producto", command=self.controlador.modificar_producto_interfaz).grid(row=3, column=5, padx=5, pady=5)

        self.tree = ttk.Treeview(frame_principal, columns=("ID", "Producto", "Descripción", "Stock"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Stock", text="Stock")
        self.tree.grid(row=4, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        
        # Menú
        menubar = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar)
        archivo_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Salir", accelerator="Ctrl+X", command=self.ventana.quit)

    def actualizar_lista(self, productos):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for producto in productos:
            self.tree.insert("", "end", values=producto)

    def mainloop(self):
        self.ventana.mainloop()
