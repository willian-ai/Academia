import customtkinter as ctk
from controllers.profesor_controller import ProfesorController
from mysql.connector import IntegrityError
from views.viewTkinter.menuPrincipal import MenuPrincipal
import re

class RegistrarProfesor:
    def __init__(self, db=None, tema_actual = "System") :
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Registrar Profesor")
        self.profesor_controller = ProfesorController(db)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
        ctk.set_default_color_theme("green")

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.8)
        alto_ventana = int(alto_pantalla * 0.8)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Profesor", font=("Helvetica", 20))
        self.titulo.pack(pady=20)

        # Crear el frame para los campos de entrada
        self.frame_campos = ctk.CTkFrame(self.root)
        self.frame_campos.pack(padx=20, pady=10, fill="both", expand=True)

        # Crear los campos de entrada
        self.lbl_nombre = ctk.CTkLabel(self.frame_campos, text="Nombre:")
        self.lbl_nombre.pack(pady=5)

        self.entry_nombre = ctk.CTkEntry(self.frame_campos, placeholder_text="Ingrese el nombre del profesor")
        self.entry_nombre.pack(pady=5)

        self.lbl_apellido = ctk.CTkLabel(self.frame_campos, text="Apellido:")
        self.lbl_apellido.pack(pady=5)

        self.entry_apellido = ctk.CTkEntry(self.frame_campos, placeholder_text="Ingrese el apellido del profesor")
        self.entry_apellido.pack(pady=5)    

        self.lbl_email = ctk.CTkLabel(self.frame_campos, text="Email:")
        self.lbl_email.pack(pady=5)

        self.entry_email = ctk.CTkEntry(self.frame_campos, placeholder_text="Ingrese el email del profesor")
        self.entry_email.pack(pady=5)   

        self.lbl_telefono = ctk.CTkLabel(self.frame_campos, text="Telefono:")
        self.lbl_telefono.pack(pady=5)

        self.entry_telefono = ctk.CTkEntry(self.frame_campos, placeholder_text="Ingrese el telefono del profesor")
        self.entry_telefono.pack(pady=5)    

        self.lbl_especialidad = ctk.CTkLabel(self.frame_campos, text="Especialidad:")
        self.lbl_especialidad.pack(pady=5)

        self.entry_especialidad = ctk.CTkEntry(self.frame_campos, placeholder_text="Ingrese la especialidad del profesor")
        self.entry_especialidad.pack(pady=5)    

        # Boton para registrar el profesor
        self.btn_registrar = ctk.CTkButton(self.frame_campos, text="Registrar", command=self.registrar_profesor)
        self.btn_registrar.pack(pady=10)

        # Boton para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.frame_campos, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(pady=10)

    def registrar_profesor(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        especialidad = self.entry_especialidad.get()

        if not self.validar_campos():
            return
        
        try:
            self.profesor_controller.registrar_profesor(nombre, apellido, email, telefono, especialidad)
            self.notificacion(mensaje="Profesor registrado correctamente")
            self.root.destroy()
            menu_principal = MenuPrincipal(self.db, self.tema_actual)
            menu_principal.root.mainloop()
        except IntegrityError as e:
            self.notificacion(mensaje=f"Error al registrar el profesor: {e}")
            print(f"Error al registrar el profesor: {e}")
        except Exception as e:
            self.notificacion(mensaje=f"Error al registrar el profesor: {e}")
            print(f"Error al registrar el profesor: {e}")
            
    def notificacion(self, mensaje=""):
        ventana_notificacion = ctk.CTk()
        ventana_notificacion.title("Notificacion")
        ventana_notificacion.geometry("300x100")
        ventana_notificacion.resizable(False, False)

        label_notificacion = ctk.CTkLabel(ventana_notificacion, text=mensaje, font=("Helvetica", 12))
        label_notificacion.pack(pady=20)

        btn_aceptar = ctk.CTkButton(ventana_notificacion, text="Aceptar", command=ventana_notificacion.destroy)
        btn_aceptar.pack(pady=10)

        ventana_notificacion.mainloop()

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()

    def validar_campos(self):
        if not self.entry_nombre.get():
            self.notificacion(mensaje="El nombre del profesor es requerido")
            return False
        if not self.entry_apellido.get():
            self.notificacion(mensaje="El apellido del profesor es requerido")
            return False
        if not self.entry_email.get() or not re.match(r"[^@]+@[^@]+\.[^@]+", self.entry_email.get()):
            self.notificacion(mensaje="El email del profesor es requerido")
            return False    
        if not self.entry_telefono.get() or not re.match(r"^\d{10}$", self.entry_telefono.get()):
            self.notificacion(mensaje="El telefono del profesor es requerido")
            return False
        if not self.entry_especialidad.get():
            self.notificacion(mensaje="La especialidad del profesor es requerida")
            return False
        return True
            
        
        
        
        


