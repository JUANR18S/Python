"""Módulo principal del sistema veterinario."""

# El import de ``clases`` debe funcionar tanto si este archivo se ejecuta como
# parte del paquete ``Sprint4`` (``Sprint4.SistemaVet``) como si se lanza de
# forma independiente desde su carpeta.  Para mantener la compatibilidad en
# ambos casos se intenta primero el import relativo y, si falla, se usa el
# absoluto.
try:  # Import cuando se usa como paquete (p.ej. ``import Sprint4.SistemaVet``)
    from .clases import Dueno, Mascota, Consulta
except ImportError:  # Import directo al ejecutar desde el propio directorio
    from clases import Dueno, Mascota, Consulta


class SistemaVeterinario:
    def __init__(self):
        self.mascotas = []
        self.duenos = []

    def registrar_paciente_completo(self):
        print("\n🐾 Registro completo de paciente 🐾")

        print("\n👤 Datos del humano a cargo:")
        nombre = input("Nombre completo: ").strip()
        documento = input("Número de documento: ").strip()
        correo = input("Correo electrónico: ").strip()
        telefono = input("Celular: ").strip()

        if not nombre or not documento or not correo or not telefono:
            print("❌ Todos los campos del dueño son obligatorios.")
            return

        dueno = Dueno(nombre, documento, correo, telefono)

        # Datos de la mascota
        print("\n🐶 Datos de la mascota:")
        nombre_mascota = input("Nombre: ").strip()
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()
        try:
            edad = int(input("Edad (en años): ").strip())
            peso = float(input("Peso (en kg): ").strip())
        except ValueError:
            print("❌ Edad y peso deben ser valores numéricos.")
            return

        motivo = input("Motivo de consulta: ").strip()

        if not nombre_mascota or not especie or not raza or not motivo:
            print("❌ Todos los campos de la mascota son obligatorios.")
            return

        mascota = Mascota(
            nombre_mascota, especie, raza, edad, peso, motivo, dueno
        )
        # Solo en este punto sabemos que el registro fue exitoso; ahora
        # agregamos al dueño y a la mascota a sus respectivas listas.
        self.duenos.append(dueno)
        self.mascotas.append(mascota)

        print("\n✅ Paciente registrado correctamente.")

    def registrar_consulta(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return

        print("\nSeleccione mascota:")
        for i, mascota in enumerate(self.mascotas, 1):
            print(f"{i}. {mascota.nombre} ({mascota.especie})")

        try:
            op = int(input("Número de mascota: ")) - 1
            if op < 0 or op >= len(self.mascotas):
                raise ValueError
            mascota = self.mascotas[op]
        except ValueError:
            print("Opción inválida.")
            return

        fecha = input("Fecha (dd/mm/aaaa): ").strip()
        motivo = input("Motivo: ").strip()
        diagnostico = input("Diagnóstico: ").strip()

        consulta = Consulta(fecha, motivo, diagnostico, mascota)
        mascota.agregar_consulta(consulta)
        print("Consulta registrada!")

    def listar_mascotas(self):
        print("\n🐶 Mascotas registradas:")
        if not self.mascotas:
            print("No hay mascotas.")
        for mascota in self.mascotas:
            print(mascota)

    def ver_historial(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
            return

        print("\nSeleccione mascota:")
        for i, mascota in enumerate(self.mascotas, 1):
            print(f"{i}. {mascota.nombre}")

        try:
            op = int(input("Número de mascota: ")) - 1
            if op < 0 or op >= len(self.mascotas):
                raise ValueError
            mascota = self.mascotas[op]
        except ValueError:
            print("Opción inválida.")
            return

        print(f"\n📋 Historial de {mascota.nombre}:")
        if not mascota.consultas:
            print("No hay consultas registradas.")
        else:
            for consulta in mascota.consultas:
                print(consulta)
