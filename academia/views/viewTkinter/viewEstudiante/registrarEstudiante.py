import customtkinter as ctk
from controllers.estudiante_controller import EstudianteController
from mysql.connector import IntegrityError
import re


class RegistrarEstudiante:
    def __init__(self, db = None, tema_actual = "System"):
        self.db = db
        self.root = ctk.CTk()
        self.tema_actual = tema_actual
        self.root.title("Registrar Estudiante")
        self.estudiante_controller = EstudianteController(db)

        # Configuracion de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la 
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.2)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}") 
        
        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Estudiante", font=("Helvetica", 20))
        self.titulo.pack(pady=20)

        # Campo de nombre
        self.nombre = ctk.CTkEntry(self.root, placeholder_text="Nombre")
        self.nombre.pack(pady=10)

        # Campo de apellido
        self.apellido = ctk.CTkEntry(self.root, placeholder_text="Apellido")
        self.apellido.pack(pady=10)

        # Campo de correo
        self.correo = ctk.CTkEntry(self.root, placeholder_text="Correo")
        self.correo.pack(pady=10)

        # Campo de telfono
        self.telefono = ctk.CTkEntry(self.root, placeholder_text="Telefono")
        self.telefono.pack(pady=10)

        # Boton para registrar
        self.boton_registrar = ctk.CTkButton(self.root, text="Registrar", command=self.registrar_estudiante)
        self.boton_registrar.pack(pady=10)

        # Boton para regresar
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()
        
    def registrar_estudiante(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        correo = self.correo.get()
        telefono = self.telefono.get()

        if not self.validar_campos():
            return
        
        try:
            self.estudiante_controller.registrar_estudiante(nombre, apellido, correo, telefono)
            self.notificacion(mensaje="Estudiante registrado correctamente")
            self.root.destroy()
            menu_principal = MenuPrincipal(self.tema_actual, self.db)
            menu_principal.root.mainloop()
        except IntegrityError as e:
            self.notificacion(mensaje="Error al registrar el estudiante")
            print(f"Error al registrar el estudiante: {e}")
        except Exception as e:
            self.notificacion(mensaje="Error al registrar el estudiante")
            print(f"Error al registrar el estudiante: {e}")

    def notificacion(self, mensaje=""):
        ventana_notificacion = ctk.CTk()
        ventana_notificacion.title("Notificacion")
        ventana_notificacion.geometry("350x120")
        ventana_notificacion.resizable(False, False)

        label_notificacion = ctk.CTkLabel(ventana_notificacion, text=mensaje, font=("Helvetica", 16))
        label_notificacion.pack(pady=20)

        btn_aceptar = ctk.CTkButton(ventana_notificacion, text="Aceptar", command=ventana_notificacion.destroy)
        btn_aceptar.pack(pady=10)

        ventana_notificacion.mainloop()

    def validar_campos(self):
        if not self.nombre.get():
            self.notificacion(mensaje="El nombre es requerido")
            return False
        if not self.apellido.get():
            self.notificacion(mensaje="El apellido es requerido")
            return False
        if not self.correo.get() or not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo.get()):
            self.notificacion(mensaje="El correo es requerido")
            return False
        if not self.telefono.get():
            self.notificacion(mensaje="El telefono es requerido")
            return False
        return True
        
            
        
        
        
        
        
        
