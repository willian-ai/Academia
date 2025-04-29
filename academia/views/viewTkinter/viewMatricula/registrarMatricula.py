import customtkinter as ctk
from tkinter import messagebox
from controllers.matricula_controller import MatriculaController
from mysql.connector import IntegrityError
from datetime import datetime

class RegistrarMatricula:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Registrar Matrícula")
        self.controller = MatriculaController(db)
        
        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        # Título de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Matrícula", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)
        
        # Frame para los campos
        self.frame_campos = ctk.CTkFrame(self.root)
        self.frame_campos.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Campo para el ID del estudiante
        self.label_estudiante = ctk.CTkLabel(self.frame_campos, text="ID del Estudiante:")
        self.label_estudiante.pack(pady=5)
        
        self.entry_estudiante = ctk.CTkEntry(self.frame_campos)
        self.entry_estudiante.pack(pady=5, fill="x")
        
        # Campo para el ID del curso
        self.label_curso = ctk.CTkLabel(self.frame_campos, text="ID del Curso:")
        self.label_curso.pack(pady=5)
        
        self.entry_curso = ctk.CTkEntry(self.frame_campos)
        self.entry_curso.pack(pady=5, fill="x")
        
        # Campo para la fecha de matrícula
        self.label_fecha = ctk.CTkLabel(self.frame_campos, text="Fecha de Matrícula (YYYY-MM-DD):")
        self.label_fecha.pack(pady=5)
        
        self.entry_fecha = ctk.CTkEntry(self.frame_campos)
        self.entry_fecha.pack(pady=5, fill="x")
        
        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=20)
        
        # Botón para registrar
        self.btn_registrar = ctk.CTkButton(self.frame_botones, text="Registrar", 
                                          command=self.registrar_matricula)
        self.btn_registrar.pack(side="left", padx=5)
        
        # Botón para regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", 
                                         command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=5)
    
    def validar_campos(self):
        # Validar que todos los campos estén llenos
        if not self.entry_estudiante.get() or not self.entry_curso.get() or not self.entry_fecha.get():
            self.mostrar_mensaje("Error", "Todos los campos son requeridos", "error")
            return False
        
        # Validar que los IDs sean números
        try:
            int(self.entry_estudiante.get())
            int(self.entry_curso.get())
        except ValueError:
            self.mostrar_mensaje("Error", "Los IDs deben ser números", "error")
            return False
        
        # Validar formato de fecha
        try:
            datetime.strptime(self.entry_fecha.get(), '%Y-%m-%d')
        except ValueError:
            self.mostrar_mensaje("Error", "El formato de fecha debe ser YYYY-MM-DD", "error")
            return False
        
        return True
    
    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje)
        else:
            messagebox.showinfo(titulo, mensaje)
    
    def registrar_matricula(self):
        if not self.validar_campos():
            return
        
        try:
            # Obtener los valores de los campos
            id_estudiante = int(self.entry_estudiante.get())
            id_curso = int(self.entry_curso.get())
            fecha_matricula = self.entry_fecha.get()
            
            # Registrar la matrícula
            self.controller.registrar_matricula(id_estudiante, id_curso, fecha_matricula)
            
            # Mostrar mensaje de éxito
            self.mostrar_mensaje("Éxito", "Matrícula registrada correctamente")
            
            # Regresar al menú principal
            self.regresar_menu_principal()
            
        except IntegrityError as e:
            self.mostrar_mensaje("Error", "Error al registrar la matrícula: " + str(e), "error")
        except Exception as e:
            self.mostrar_mensaje("Error", "Error al registrar la matrícula: " + str(e), "error")
    
    def regresar_menu_principal(self):
        from views.viewTkinter.viewMatricula.menuMatricula import MenuMatricula
        self.root.destroy()
        menu_matricula = MenuMatricula(db=self.db, tema_actual=self.tema_actual)
        menu_matricula.root.mainloop() 