import customtkinter as ctk


class MenuEstudiante:
    def __init__(self, parent_frame):
        self.frame = parent_frame
        
        # Limpiar el frame actual
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Titulo del frame
        self.titulo_ventana = ctk.CTkLabel(self.frame, text="Menu Estudiante", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo_ventana.pack(pady=20)

        # Configuracion del tema de la ventana
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # Restriccion de la ventana
        self.frame.resizable(False, False)

        # Botonn para regresar al menu principal

         
