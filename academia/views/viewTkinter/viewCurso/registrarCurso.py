import customtkinter as ctk
from controllers.curso_controller import CursoController
from mysql.connector import IntegrityError
import re

class RegistrarCurso:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Registrar Curso")
        self.curso_controller = CursoController(db)

        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.2)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Curso", font=("Helvetica", 20))
        self.titulo.pack(pady=20)

        # Campo de nombre del curso
        self.nombre = ctk.CTkEntry(self.root, placeholder_text="Nombre")
        self.nombre.pack(pady=10)

        # Campo de descripción
        self.descripcion = ctk.CTkEntry(self.root, placeholder_text="Descripción")
        self.descripcion.pack(pady=10)

        # Campo de duración
        self.duracion = ctk.CTkEntry(self.root, placeholder_text="Duración (horas)")
        self.duracion.pack(pady=10)

        # Campo de ID del profesor
        self.profesor_id = ctk.CTkEntry(self.root, placeholder_text="ID del Profesor")
        self.profesor_id.pack(pady=10)

        # Boton para registrar
        self.boton_registrar = ctk.CTkButton(self.root, text="Registrar", command=self.registrar_curso)
        self.boton_registrar.pack(pady=10)

        # Boton para regresar
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()

    def registrar_curso(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        nombre = self.nombre.get()
        descripcion = self.descripcion.get()
        duracion = self.duracion.get()
        profesor_id = self.profesor_id.get()

        if not self.validar_campos():
            return

        try:
            self.curso_controller.registrar_curso(nombre, descripcion, duracion, profesor_id)
            self.notificacion(mensaje="Curso registrado correctamente")
            self.root.destroy()
            menu_principal = MenuPrincipal(self.tema_actual, self.db)
            menu_principal.root.mainloop()
        except IntegrityError as e:
            self.notificacion(mensaje="Error al registrar el curso")
            print(f"Error al registrar el curso: {e.msg}")
        except Exception as e:
            self.notificacion(mensaje="Error al registrar el curso")
            print(f"Error al registrar el curso: {e}")

    def validar_campos(self):
        if not self.nombre.get() or not self.descripcion.get() or not self.duracion.get() or not self.profesor_id.get():
            self.notificacion(mensaje="Por favor complete todos los campos")
            return False
        try:
            int(self.duracion.get())
            int(self.profesor_id.get())
        except ValueError:
            self.notificacion(mensaje="La duración y el ID del profesor deben ser números")
            return False
        return True

    def notificacion(self, mensaje=""):
        ventana_notificacion = ctk.CTk()
        ventana_notificacion.title("Notificación")
        ventana_notificacion.geometry("300x150")
        ventana_notificacion.resizable(False, False)

        label_notificacion = ctk.CTkLabel(ventana_notificacion, text=mensaje, font=("Helvetica", 16))
        label_notificacion.pack(pady=20)

        btn_aceptar = ctk.CTkButton(ventana_notificacion, text="Aceptar", command=ventana_notificacion.destroy)
        btn_aceptar.pack(pady=10)

        ventana_notificacion.mainloop() 