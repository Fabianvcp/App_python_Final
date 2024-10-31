from controller.controlador import Controlador
from model.modelo import Modelo
from view.vista import Vista

def main():
    # Crear instancia del modelo
    modelo = Modelo()

    # Crear instancia del controlador, asignándole el modelo
    controlador = Controlador(modelo)

    # Crear instancia de la vista, asignándole el controlador
    vista = Vista(controlador)
    vista.actualizar()
    
    # Ejecutar la interfaz de usuario
    vista.mainloop()

if __name__ == "__main__":
    main()