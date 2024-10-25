# Todo lo relacionado a la Vista
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.controlador.asignar_vista(self)  # Asignar la vista al controlador
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Stock")
        self.ventana.geometry("880x650")
        self.ventana.configure(bg="#DCE3F1")  # Fondo de la ventana en azul claro
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear el marco principal con colores y relleno
        frame_principal = tk.Frame(self.ventana, bg="#DCE3F1", padx=10, pady=10)
        frame_principal.pack(fill="both", expand=True)

        # Estilo personalizado para botones y entradas
        estilo_botones = {"bg": "#0066CC", "fg": "white", "font": ("Arial", 10, "bold")}
        estilo_entradas = {"bg": "#F0F5FF", "fg": "#333", "font": ("Arial", 10)}
        
        tk.Label(frame_principal, text="Producto:", bg="#DCE3F1", fg="#003366", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        self.entrada_producto = tk.Entry(frame_principal)
        self.entrada_producto.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_principal, text="Descripción:", bg="#DCE3F1", fg="#003366", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
        self.entrada_descripcion = tk.Entry(frame_principal)
        self.entrada_descripcion.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_principal, text="Stock:", bg="#DCE3F1", fg="#003366", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5)
        self.entrada_stock = tk.Entry(frame_principal)
        self.entrada_stock.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Button(frame_principal, text="Agregar Producto", command=self.controlador.agregar_producto_interfaz, **estilo_botones).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(frame_principal, text="Buscar Producto", command=self.controlador.buscar_producto_interfaz, **estilo_botones).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(frame_principal, text="Borrar Producto", command=self.controlador.borrar_producto_interfaz, **estilo_botones).grid(row=3, column=3, padx=5, pady=5)
        tk.Button(frame_principal, text="Vender Producto", command=self.controlador.vender_producto_interfaz, **estilo_botones).grid(row=3, column=4, padx=5, pady=5)
        tk.Button(frame_principal, text="Modificar Producto", command=self.controlador.modificar_producto_interfaz, **estilo_botones).grid(row=3, column=5, padx=5, pady=5)
        
        self.tree = ttk.Treeview(frame_principal, columns=("ID", "Producto", "Descripción", "Stock"), show="headings")
        
        estilo_tree = ttk.Style()
        estilo_tree.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#003366", foreground="black")
        estilo_tree.configure("Treeview", rowheight=25, font=("Arial", 10))
        self.tree.heading("ID", text="ID")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Stock", text="Stock")
        self.tree.grid(row=4, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")        
        self.tree.bind("<<TreeviewSelect>>", self.cargar_producto_seleccionado)
        
        # Menú
        menubar = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar)
        archivo_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Salir", accelerator="Ctrl+X", command=self.ventana.quit)



    def actualizar(self):
        """Método que actualiza la lista de productos en la vista."""
        productos = self.controlador.obtener_productos()
        self.actualizar_lista(productos)

    def actualizar_lista(self, productos):
        """Actualizar los productos mostrados en el Treeview."""
        # Limpiar el contenido actual del Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insertar los nuevos productos
        for producto in productos:
            self.tree.insert("", "end", values=producto)

    def obtener_producto_seleccionado(self):
        """Obtener el ID del producto seleccionado en el Treeview."""
        try:
            selected_item = self.tree.selection()[0]
            return self.tree.item(selected_item)['values'][0]
        except IndexError:
            messagebox.showerror("Error", "Por favor, selecciona un producto.")
            return None
        
    def cargar_producto_seleccionado(self, event):
        """Cargar el producto seleccionado en los campos de entrada."""
        selected_item = self.tree.selection()
        if selected_item:
            producto = self.tree.item(selected_item[0])['values']
            self.entrada_producto.delete(0, tk.END)  # Limpiar el campo
            self.entrada_producto.insert(0, producto[1])  # Nombre del producto
            self.entrada_descripcion.delete(0, tk.END)  # Limpiar el campo
            self.entrada_descripcion.insert(0, producto[2])  # Descripción
            self.entrada_stock.delete(0, tk.END)  # Limpiar el campo
            self.entrada_stock.insert(0, producto[3])  # Stock
            
    def mainloop(self):
        self.ventana.mainloop()
