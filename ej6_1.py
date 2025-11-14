# =========================
# Ejercicio 1 - Tema 3 - POO
# Clases Camion y Caja + Flujo del programa
# =========================

class Caja:
    def __init__(self, codigo, peso_kg, descripcion_carga, largo, ancho, altura):
        self.codigo = codigo
        self.peso_kg = peso_kg
        self.descripcion_carga = descripcion_carga
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def __str__(self):
        return (f"Caja {self.codigo} | {self.descripcion_carga} | "
                f"Peso: {self.peso_kg} kg | Dimensiones: {self.largo}x{self.ancho}x{self.altura}")


class Camion:
    def __init__(self, matricula, conductor, capacidad_kg, descripcion_carga, rumbo, velocidad):
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = descripcion_carga
        self.rumbo = rumbo
        self.velocidad = velocidad
        self.cajas = []

    def peso_total(self):
        return sum(caja.peso_kg for caja in self.cajas)

    def add_caja(self, caja):
        if self.peso_total() + caja.peso_kg <= self.capacidad_kg:
            self.cajas.append(caja)
        else:
            print(f"No se puede añadir la caja {caja.codigo}, supera la capacidad del camión.")

    def setVelocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad

    def setRumbo(self, nuevo_rumbo):
        if 1 <= nuevo_rumbo <= 359:
            self.rumbo = nuevo_rumbo
        else:
            print("Rumbo inválido. Debe estar entre 1 y 359 grados.")

    def claxon(self):
        print("piiiiiii")

    def __str__(self):
        info_cajas = "\n".join(str(caja) for caja in self.cajas)
        return (f"Camión {self.matricula} | Conductor: {self.conductor} | "
                f"Capacidad: {self.capacidad_kg} kg | Rumbo: {self.rumbo}° | "
                f"Velocidad: {self.velocidad} km/h | Nº Cajas: {len(self.cajas)} | "
                f"Peso total: {self.peso_total()} kg\n"
                f"Cajas:\n{info_cajas}")


# =========================
# Flujo del programa
# =========================
if __name__ == "__main__":
    # Crear cajas
    c1 = Caja("C1", 100, "Electrónica", 1.0, 0.5, 0.3)
    c2 = Caja("C2", 200, "Ropa", 1.2, 0.8, 0.5)
    c3 = Caja("C3", 150, "Alimentos", 1.5, 0.7, 0.4)

    c4 = Caja("C4", 120, "Libros", 1.0, 0.6, 0.4)
    c5 = Caja("C5", 180, "Muebles", 2.0, 1.0, 0.8)
    c6 = Caja("C6", 90, "Juguetes", 0.8, 0.5, 0.3)

    # Crear camiones
    camion1 = Camion("1234ABC", "Juan", 1000, "Carga variada", 90, 80)
    camion2 = Camion("5678DEF", "Pedro", 800, "Carga ligera", 180, 60)

    # Añadir 3 cajas a cada camión
    for caja in [c1, c2, c3]:
        camion1.add_caja(caja)

    for caja in [c4, c5, c6]:
        camion2.add_caja(caja)

    # Mostrar información inicial
    print("=== Estado inicial ===")
    print(camion1)
    print(camion2)

    # Añadir más cajas
    camion1.add_caja(Caja("C7", 200, "Herramientas", 1.0, 0.5, 0.5))
    camion1.add_caja(Caja("C8", 300, "Material construcción", 2.0, 1.5, 1.0))

    camion2.add_caja(Caja("C9", 100, "Papelería", 1.0, 0.5, 0.3))
    camion2.add_caja(Caja("C10", 150, "Electrodomésticos", 1.5, 1.0, 0.7))
    camion2.add_caja(Caja("C11", 200, "Plásticos", 2.0, 1.0, 0.8))

    # Cambiar velocidad y rumbo
    camion1.setVelocidad(100)
    camion1.setRumbo(120)

    camion2.setVelocidad(70)
    camion2.setRumbo(200)

    # Claxon del segundo camión
    camion2.claxon()

    # Mostrar información final
    print("\n=== Estado final ===")
    print(camion1)
    print(camion2)
