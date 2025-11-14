import tkinter as tk
import math
import pygame
from PIL import Image, ImageTk  # para cargar imágenes de camiones

# ---------------- CLASES ----------------
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
    def __init__(self, matricula, conductor, capacidad_kg, descripcion_carga, rumbo, velocidad, x=50, y=50, sprite=None):
        self.matricula = matricula
        self.conductor = conductor
        self.capacidad_kg = capacidad_kg
        self.descripcion_carga = descripcion_carga
        self.rumbo = rumbo
        self.velocidad = velocidad
        self.cajas = []
        self.x = x
        self.y = y
        self.sprite = sprite  # imagen del camión

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
        pygame.mixer.init()
        pygame.mixer.music.load("claxon.mp3")  
        pygame.mixer.music.play()

    def mover(self):
        rad = math.radians(self.rumbo)
        self.x += math.cos(rad) * (self.velocidad / 10)
        self.y += math.sin(rad) * (self.velocidad / 10)

    def __str__(self):
        info_cajas = "\n".join(str(caja) for caja in self.cajas)
        return (f"Camión {self.matricula} | Conductor: {self.conductor} | "
                f"Capacidad: {self.capacidad_kg} kg | Rumbo: {self.rumbo}° | "
                f"Velocidad: {self.velocidad} km/h | Nº Cajas: {len(self.cajas)} | "
                f"Peso total: {self.peso_total()} kg\n"
                f"Cajas:\n{info_cajas}")


# ---------------- INTERFAZ ----------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Camiones 🚚")

        # Canvas para dibujar
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightgray")
        self.canvas.pack()

        # Cargar imagen del camión
        img = Image.open("camion.png")  # pon aquí tu sprite de camión
        img = img.resize((60, 40))  # ajustar tamaño
        self.camion_img = ImageTk.PhotoImage(img)

        # Crear camiones
        self.camiones = [
            Camion("1234ABC", "Juan", 1000, "Carga variada", 45, 20, x=100, y=200, sprite=self.camion_img),
            Camion("5678DEF", "Pedro", 800, "Carga ligera", 135, 15, x=300, y=100, sprite=self.camion_img)
        ]
        self.camion_activo = self.camiones[0]

        # Selector de camión
        self.selector = tk.StringVar(value=self.camion_activo.matricula)
        tk.OptionMenu(root, self.selector, *[c.matricula for c in self.camiones], command=self.seleccionar_camion).pack()

        # Botones de control
        tk.Button(root, text="Añadir Caja", command=self.anadir_caja).pack()
        tk.Button(root, text="Aumentar Velocidad", command=self.aumentar_velocidad).pack()
        tk.Button(root, text="Cambiar Rumbo", command=self.cambiar_rumbo).pack()
        tk.Button(root, text="Claxon", command=self.tocar_claxon).pack()

        # Área de información
        self.info = tk.Text(root, width=80, height=10)
        self.info.pack()

        # Iniciar animación
        self.animar()

    def seleccionar_camion(self, matricula):
        for c in self.camiones:
            if c.matricula == matricula:
                self.camion_activo = c
                self.mostrar_info()

    def mostrar_info(self):
        self.info.delete("1.0", tk.END)
        self.info.insert(tk.END, str(self.camion_activo))

    def anadir_caja(self):
        caja = Caja(f"C{len(self.camion_activo.cajas)+1}", 100, "Carga genérica", 1, 1, 1)
        self.camion_activo.add_caja(caja)
        self.mostrar_info()

    def aumentar_velocidad(self):
        self.camion_activo.setVelocidad(self.camion_activo.velocidad + 5)
        self.mostrar_info()

    def cambiar_rumbo(self):
        nuevo_rumbo = (self.camion_activo.rumbo + 45) % 360
        self.camion_activo.setRumbo(nuevo_rumbo)
        self.mostrar_info()

    def tocar_claxon(self):
        self.camion_activo.claxon()

    def animar(self):
        self.canvas.delete("all")
        for c in self.camiones:
            c.mover()
            # dibujar sprite
            self.canvas.create_image(c.x, c.y, image=c.sprite, anchor="center")
            self.canvas.create_text(c.x, c.y-30, text=c.matricula)
        self.root.after(100, self.animar)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
