import customtkinter as ctk
from .viewEstudiante.menuEstudiante import MenuEstudiante
from .viewProfesor.menuProfesor import MenuProfesor
from .viewCurso.menuCurso import MenuCurso
from .viewHorario.menuHorario import MenuHorario
# Crear la clase principal de la ventana la cual se encargara de mostrar el menu principal
class MenuPrincipal:
   
    def __init__(self, db = None, tema_actual = "System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Menu Principal")
        # Configuración del tema
        ctk.set_appearance_mode(tema_actual)
        ctk.set_default_color_theme("green")

        
        ancho_ventana = int(self.root.winfo_screenwidth() * 0.2)
        alto_ventana = int(self.root.winfo_screenheight() * 0.45)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
    
        #  Restriccion de la ventana
        self.root.resizable(False, False)

        # Coordenadas centradas de la ventana
        x = (ancho_ventana // 2) - (ancho_ventana // 2)
        y = (alto_ventana // 2) - (alto_ventana // 2)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        self.titulo = ctk.CTkLabel(self.root, text="Menu Principal", font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=20)

        botones = [
            ("Estudiantes", self.abrir_ventana_estudiantes),
            ("Profesores", self.abrir_ventana_profesores),
            ("Cursos", self.abrir_ventana_cursos),
            ("Matriculas", self.abrir_ventana_matriculas),
            ("Horarios", self.abrir_ventana_horarios)
        ]
        
        for i, (text, command) in enumerate(botones):
            btn = ctk.CTkButton(self.root, text=text, command=command)
            btn.pack(pady=10, padx=20)

        # Frame 
        self.tema_actual = "System"
        self.btn_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(pady=20)

    def abrir_ventana_estudiantes(self):
        self.root.destroy()
        menu_estudiante = MenuEstudiante(db = self.db, tema_actual = self.tema_actual)
        menu_estudiante.root.mainloop()
    
    def abrir_ventana_profesores(self):
        self.root.destroy()
        menu_profesor = MenuProfesor(db = self.db, tema_actual = self.tema_actual)
        menu_profesor.root.mainloop()
    
    def abrir_ventana_cursos(self):
        self.root.destroy()
        menu_curso = MenuCurso(db = self.db, tema_actual = self.tema_actual)
        menu_curso.root.mainloop()

    def abrir_ventana_matriculas(self):
        #self.root.destroy()
        #menu_matricula = MenuMatricula(db = self.db, tema_actual = self.tema_actual)
        #menu_matricula.root.mainloop()
        pass

    def abrir_ventana_horarios(self):
        self.root.destroy()
        menu_horario = MenuHorario(db = self.db, tema_actual = self.tema_actual)
        menu_horario.root.mainloop()
        

    def cambiar_tema(self):
        if self.tema_actual =="Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"
        

    
    
    
    
