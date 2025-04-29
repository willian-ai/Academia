import customtkinter as ctk
from controllers.horario_controller import HorarioController
from mysql.connector import IntegrityError
import re

class RegistrarHorario:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Registrar Horario")
        self.controller = HorarioController(db)

        # Configuracion de la ventana
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
        self.titulo = ctk.CTkLabel(self.root, text="Registrar Horario", font=("Helvetica", 20))
        self.titulo.pack(pady=20)
        
        # Campo del dia de la semana
        self.dia_semana = ctk.CTkEntry(self.root, placeholder_text="Día de la semana")
        self.dia_semana.pack(pady=10)

        # Campo de la hora de inicio
        self.hora_inicio = ctk.CTkEntry(self.root, placeholder_text="Hora de inicio")
        self.hora_inicio.pack(pady=10)

        # Campo de la hora de fin
        self.hora_fin = ctk.CTkEntry(self.root, placeholder_text="Hora de fin")
        self.hora_fin.pack(pady=10)

        # Campo del ID del curso    
        self.curso_id = ctk.CTkEntry(self.root, placeholder_text="ID del curso")
        self.curso_id.pack(pady=10)

        # Boton para registrar
        self.boton_registrar = ctk.CTkButton(self.root, text="Registrar", command=self.registrar_horario)
        self.boton_registrar.pack(pady=10)

        #  Campo del boton para regresar
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()

    def registrar_horario(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        dia_semana = self.dia_semana.get()
        hora_inicio = self.hora_inicio.get()
        hora_fin = self.hora_fin.get()
        curso_id = self.curso_id.get()

        if not self.validar_campos():
            return
        
        try:
            self.controller.registrar_horario(curso_id, dia_semana, hora_inicio, hora_fin)
            self.notificacion(mensaje="Horario registrado correctamente")
            self.root.destroy()
            menu_principal = MenuPrincipal(self.tema_actual, self.db)
            menu_principal.root.mainloop()
        
        except IntegrityError as e:
            self.notificacion(mensaje="Error al registrar el horario")
            print(f"Error al registrar el horario: {e.msg}")
        except Exception as e:
            self.notificacion(mensaje="Error al registrar el horario")
            print(f"Error al registrar el horario: {e}")

    def validar_campos(self):
        if not self.dia_semana.get() or not self.hora_inicio.get() or not self.hora_fin.get() or not self.curso_id.get():
            self.notificacion(mensaje="Por favor complete todos los campos")
            return False
        try:
            int(self.curso_id.get())
        except ValueError:
            self.notificacion(mensaje="El ID del curso debe ser un número")
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
        
        
