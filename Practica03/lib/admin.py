from Practica03.lib.buses import *
from Practica03.lib.conductores import *

class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self):
        placa_bus = input("Ingrese la placa del bus: ")
        if placa_bus in self.buses:
            print("Error: La placa del bus ya existe.")
            return

        self.buses[placa_bus] = Bus(placa_bus)
        print(f"Bus {placa_bus} agregado correctamente.")

    def agregar_ruta_a_bus(self):
        placa_bus = input("Ingrese la placa del bus: ")
        if placa_bus not in self.buses:
            print("Error: Bus no encontrado.")
            return

        ruta = input("Ingrese la ruta del bus: ")
        self.buses[placa_bus].asignar_ruta(ruta)
        print(f"Ruta asignada al bus {placa_bus} correctamente.")

    def registrar_horario_bus(self):
        placa_bus = input("Ingrese la placa del bus: ")
        if placa_bus not in self.buses:
            print("Error: Bus no encontrado.")
            return

        try:
            horario_ingreso = int(input("Ingrese la hora de ingreso del bus (0-23): "))
            horario_salida = int(input("Ingrese la hora de salida del bus (0-23): "))
            if not self.buses[placa_bus].registrar_horario(horario_ingreso, horario_salida):
                raise ValueError
        except ValueError:
            print("Error: Horarios inválidos. Debe ingresar un rango válido (0-23).")
            return

        print(f"Horario {horario_ingreso}:00 - {horario_salida}:00 registrado para el bus {placa_bus}.")

    def agregar_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        self.conductores[nombre] = Conductor(nombre)
        print(f"Conductor {nombre} agregado correctamente.")

    def asignar_horario_conductor(self):

        nombre = input("Ingrese el nombre del conductor: ")
        if nombre not in self.conductores:
            print("Error: Conductor no encontrado.")
            return
       
        try:
            horario_inicio = int(input("Ingrese la hora de inicio de trabajo (0-23): "))
            horario_fin = int(input("Ingrese la hora de fin de trabajo (0-23): "))
            if not self.conductores[nombre].asignar_horario(horario_inicio, horario_fin):
                raise ValueError
        except ValueError:
            print("Error: Horarios inválidos. Debe ingresar un rango válido (0-23).")
            return

        print(f"Horario {horario_inicio}:00 - {horario_fin}:00 asignado al conductor {nombre}.")

    def asignar_bus_a_conductor(self):
        placa_bus = input("Ingrese la placa del bus: ")
        if placa_bus not in self.buses:
            print("Error: Bus no encontrado.")
            return
    
        nombre = input("Ingrese el nombre del conductor: ")
        if nombre not in self.conductores:
            print("Error: Conductor no encontrado.")
            return
    
        conductor = self.conductores[nombre]
        if not hasattr(conductor, 'horario_inicio') or not hasattr(conductor, 'horario_fin'):
            print("Error: El conductor no tiene un horario asignado.")
            return
    
        horario_inicio = conductor.horario_inicio
        horario_fin = conductor.horario_fin
    
        if not self.buses[placa_bus].asignar_conductor(conductor, horario_inicio, horario_fin):
            print("Error: No se pudo asignar el conductor en el horario indicado.")
        else:
            print(f"Conductor {nombre} asignado al bus {placa_bus} de {horario_inicio}:00 a {horario_fin}:00 correctamente.")
            
