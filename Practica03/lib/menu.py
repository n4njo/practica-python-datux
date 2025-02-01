from Practica03.lib.admin import *

def menu():
    admin = Admin()
    while True:
        print(
            """
                Bienvenido a la gestión de tickets de buses
            
                1. Agregar bus
                2. Agregar ruta al bus
                3. Registrar horario al bus
                4. Agregar conductor
                5. Agregar horario del conductor
                6. Asignar bus al conductor
                7. Salir
            """
        )

        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1": 
                admin.agregar_bus()
            case "2": 
                admin.agregar_ruta_a_bus()
            case "3": 
                admin.registrar_horario_bus()
            case "4": 
                admin.agregar_conductor()
            case "5": 
                admin.asignar_horario_conductor()
            case "6": 
                admin.asignar_bus_a_conductor()
            case "7":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                