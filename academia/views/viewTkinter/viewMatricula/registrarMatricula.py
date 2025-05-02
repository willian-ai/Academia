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
        ancho_ventana = int(ancho_pantalla * 0.2)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        # Título de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Matrícula", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)
        
        # Campo para el ID del estudiante
        self.id_estudiante = ctk.CTkEntry(self.root, placeholder_text="Estudiante:")
        self.id_estudiante.pack(pady=10)
                    
        # Campo para el ID del curso
        self.id_curso = ctk.CTkEntry(self.root, placeholder_text="Curso:")
        self.id_curso.pack(pady=5)
                
        # Campo para la fecha de matrícula
        self.lbl_fecha = ctk.CTkEntry(self.root, placeholder_text="Fecha de Matrícula (YYYY-MM-DD):")
        self.lbl_fecha.pack(pady=5)
        
              
                # Botón para registrar
        self.btn_registrar = ctk.CTkButton(self.root, text="Registrar", 
                                          command=self.registrar_matricula)
        self.btn_registrar.pack(pady=10)
        
        # Botón para regresar
        self.btn_regresar = ctk.CTkButton(self.root, text="Regresar", 
                                         command=self.regresar_menu_principal)
        self.btn_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from views.viewTkinter.viewMatricula.menuMatricula import MenuMatricula
        self.root.destroy()
        menu_matricula = MenuMatricula(db=self.db, tema_actual=self.tema_actual)
        menu_matricula.root.mainloop() 


    def registrar_matricula(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        id_estudiante = self.id_estudiante.get()
        idcurso = self.id_curso.get()
        lbl_fecha = self.lbl_fecha.get()
        
        if not self.validar_campos():
            return
        
        try:
            self.controller.registrar_matricula(id_estudiante, idcurso, lbl_fecha)
            self.notificacion(mensaje="Matrícula registrada correctamente")
            self.root.destroy()
            menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
            menu_principal.root.mainloop()

        except IntegrityError as e:
            self.notificacion(mensaje="Error al registrar la matrícula ")
            print(f"Error al registrar la matrícula: {e.msg}")
            self.limpiar_campos()

        except Exception as e:
            self.notificacion(mensaje="Error al registrar la matrícula ")
            print(f"Error al registrar la matrícula: {e}")
           
    def notificacion(self, mensaje=""):
        ventana_notoficacion = ctk.CTk()
        ventana_notoficacion.title("Notificación")
        ventana_notoficacion.geometry("300x100")
        ventana_notoficacion.resizable(False, False)

        label_notificacion = ctk.CTkLabel(ventana_notoficacion, text=mensaje, font=("Arial", 16))
        label_notificacion.pack(pady=10)

        btn_aceptar = ctk.CTkButton(ventana_notoficacion, text="Aceptar", command=ventana_notoficacion.destroy)
        btn_aceptar.pack(pady=10)
        ventana_notoficacion.mainloop()


    def validar_campos(self):
        # Validar que todos los campos estén llenos
        if not self.id_estudiante.get() or not self.id_curso.get() or not self.lbl_fecha.get():
            self.notificacion(mensaje= "Todos los campos son requeridos")
            return False
        if not self.id_estudiante.get().isdigit() or not self.id_curso.get().isdigit():
            self.notificacion(mensaje= "Los IDs deben ser números")
            return False
        # Validar el formato de fecha YYYY-MM-DD
        try:
            datetime.strptime(self.lbl_fecha.get(), "%Y-%m-%d")
        # Si llegamos aquí, el formato de fecha es correcto.
        except ValueError:
        # Si ocurre un ValueError, el formato no es correcto.
            self.notificacion(mensaje= "El formato de fecha debe ser YYYY-MM-DD")
            return False
    # Si todas las validaciones anteriores pasaron, retorna True
        return True
    
    def limpiar_campos(self):
        self.id_estudiantedelete(0, ctk.END)
        self.id_curso.delete(0, ctk.END)
        self.lbl_fecha.delete(0, ctk.END)

