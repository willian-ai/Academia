import customtkinter as ctk
from PIL import Image
import os
from views.viewTkinter.viewEstudiante.menuEstudiante import MenuEstudiante

# Crear la clase principal de la ventana la cual se encargara de mostrar el menu principal
class MenuPrincipal:
   
    def __init__(self):
        # Configuración del tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Crear la ventana principal
        self.ventana = ctk.CTk()
        self.ventana.title("Sistema Académico")
        ancho_ventana = int(self.ventana.winfo_screenwidth() * 0.8)
        alto_ventana = int(self.ventana.winfo_screenheight() * 0.8)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
    
        # Crear el frame lateral izquierdo
        self.sidebar = ctk.CTkFrame(self.ventana, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Título del sidebar
        self.logo_label = ctk.CTkLabel(self.sidebar, text="Sistema Academia", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20)

        #  Restriccion de la ventana
        self.ventana.resizable(False, False)

        botones = [
            ("Estudiante", self.menu_estudiante),
            ("Profesor", self.menu_profesor),
            ("Curso", self.menu_curso),
            ("Matricula", self.menu_matricula),
            ("Horario", self.menu_horario)
        ]
        
        for i, (text, command) in enumerate(botones):
            btn = ctk.CTkButton(self.sidebar, text=text, command=command)
            btn.pack(pady=10, padx=20)


        # Frame principal
        self.main_frame = ctk.CTkFrame(self.ventana)
        self.main_frame.pack(side="left", fill="both", expand=True)

        # Título de bienvenida en el frame principal
        self.welcome_label = ctk.CTkLabel(
            self.main_frame, 
            text="Bienvenido al Sistema de Academia",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.welcome_label.pack(pady=20)

    def menu_estudiante(self):
        # Placeholder para la función de menú estudiante
        ventana_estudiante = MenuEstudiante(self.ventana)
        ventana_estudiante.ventana.mainloop()
    
    def menu_profesor(self):
        # Placeholder para la función de menú profesor
        pass
    
    def menu_curso(self):
        # Placeholder para la función de menú curso
        pass
    
    def menu_matricula(self):
        # Placeholder para la función de menú matrícula
        pass
    
    def menu_horario(self):
        # Placeholder para la función de menú horario
        pass
       


