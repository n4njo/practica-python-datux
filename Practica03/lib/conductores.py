class Conductor:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def asignar_horario(self, horario_inicio, horario_fin):
        if 0 <= horario_inicio < horario_fin <= 23:
            self.horario_inicio = horario_inicio
            self.horario_fin = horario_fin
            return True
        return False
    
    def __str__(self):
        return f"{self.nombre} | Horarios: {self.horario_inicio}:00 - {self.horario_fin}:00"
    