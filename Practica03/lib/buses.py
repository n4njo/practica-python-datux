class Bus:
    
    def __init__(self, placa_bus):
        self.placa_bus = placa_bus
        self.ruta = None
        self.horario_ingreso = None
        self.horario_salida = None
        self.horarios_conductores = [] 

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario_ingreso, horario_salida):
        if 0 <= horario_ingreso < horario_salida <= 23:
            self.horario_ingreso = horario_ingreso
            self.horario_salida = horario_salida
            return True
        return False
    
    def asignar_conductor(self, conductor, horario_inicio, horario_fin):
        if not (self.horario_ingreso <= horario_inicio < horario_fin <= self.horario_salida):
            return False  

        for (inicio, fin, _) in self.horarios_conductores:
            if not (horario_fin <= inicio or horario_inicio >= fin):
                return False  

        self.horarios_conductores.append((horario_inicio, horario_fin, conductor))
        return True

    def __str__(self):
        ruta_info = f"Ruta: {self.ruta}" if self.ruta else "Sin ruta asignada"
        conductor_info = f"Conductor: {self.conductor.nombre}" if self.conductor else "Sin conductor asignado"
        return f"Placa {self.placa_bus} | {ruta_info} | {conductor_info} | Horarios: {sorted(self.horarios)}"
    