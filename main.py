from controller.controlador import Controlador
from model.modelo import Modelo
from view.vista import Vista

def main():
    modelo = Modelo()
    controlador = Controlador(modelo)
    vista = Vista(controlador)
    
    controlador.asignar_vista(vista)  # Asignar la vista al controlador
    controlador.actualizar_lista()      # Actualizar la lista de productos inicialmente
    vista.mainloop()                    # Iniciar el bucle principal de la interfaz

if __name__ == "__main__":
    main()
