import socket

def conectaralservidor(mensaje):
    servidor_ip = '127.0.0.1'
    servidor_puerto = 500
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((servidor_ip, servidor_puerto))
        client_socket.send(mensaje.encode())
        respuesta = client_socket.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")

    finally:
        client_socket.close()

def menu_cliente():
    while True:
        print("\nMenu de Opciones:")
        print("1. Consultar todos los productos")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mensaje = "consultar_todos"
            conectaralservidor(mensaje)

        elif opcion == "2":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")
menu_cliente()