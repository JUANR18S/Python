# Definición de clases para el sistema veterinario

class Dueno:
    def __init__(self, nombre, documento, correo, telefono):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - Doc: {self.documento} - Tel: {self.telefono}"


class Mascota:
    def __init__(self, nombre, especie, raza,
                 edad, peso, motivo, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.motivo = motivo
        self.dueno = dueno
        self.consultas = []

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)

    def __str__(self):
        return (
            f"{self.nombre} ({self.especie}, {self.raza}, {self.edad} años, "
            f"{self.peso}kg) - Dueño: {self.dueno.nombre}"
        )


class Consulta:
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self):
        return (
            f"Consulta [{self.fecha}]: {self.motivo} - "
            f"Diagnóstico: {self.diagnostico}"
        )
