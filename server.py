import socket
import threading
import sqlite3

def obtener_productos():
        conexion = sqlite3.connect("stock.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos

def handle_client(client_socket):
    # Recibimos el mensaje del cliente
    mensaje = client_socket.recv(1024).decode()
    
    if mensaje.startswith("consultar_todos"):
        # Consultar todos los productos
        productos = obtener_productos()
        respuesta = f"Productos: {productos}"
    else:
        respuesta = "Comando no válido"
    
    # Enviar la respuesta al cliente
    client_socket.send(respuesta.encode())
    client_socket.close()

def start_server():
    servidor_ip = '127.0.0.1'
    servidor_puerto = 500
    
    # Crear el socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((servidor_ip, servidor_puerto))
    server.listen(5)
    print(f"Servidor escuchando en {servidor_ip}:{servidor_puerto}...")

    # Aceptar conexiones entrantes
    while True:
        client_socket, addr = server.accept()
        print(f"Conexión recibida de {addr}")
        # Crear un hilo para manejar la solicitud del cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()