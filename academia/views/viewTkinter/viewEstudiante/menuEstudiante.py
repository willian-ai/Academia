import customtkinter as ctk


class MenuEstudiante:
    def __init__(self, db = None, tema_actual = "System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Menú Estudiante")

        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Configuracion de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.8)
        alto_ventana = int(alto_pantalla * 0.8)
        self.root.geometry(f"{ancho_pantalla}x{alto_pantalla}")

      # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Menu Estudiante", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo_ventana.pack(pady=20)

      #Boton para cambiar el tema
        self.tema_actual = "System"
        self.boton_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.boton_cambiar_tema.pack(pady=20)

        # Boton para listar estudiantes en una ventana emergente que tenga una tabla
        self.boton_listar_estudiantes = ctk.CTkButton(self.root, text="Listar Estudiantes", command=self.listar_estudiantes)
        self.boton_listar_estudiantes.pack(pady=20)

        #Boton para registrar estudiante
        self.boton_registrar_estudiante = ctk.CTkButton(self.root, text="Registrar Estudiante", command=self.registrar_estudiante)
        self.boton_registrar_estudiante.pack(pady=20)

        # Boton para actualizar estudiante
        self.boton_actualizar_estudiante = ctk.CTkButton(self.root, text="Actualizar Estudiante", command=self.actualizar_estudiante)
        self.boton_actualizar_estudiante.pack(pady=20)

        # Boton para eliminar estudiante
        self.boton_eliminar_estudiante = ctk.CTkButton(self.root, text="Eliminar Estudiante", command=self.eliminar_estudiante)
        self.boton_eliminar_estudiante.pack(pady=20)
        

      #Boton para regresar al menu principal
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=20)

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()

    def cambiar_tema(self):
        if self.tema_actual == "Light":
            self.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            self.set_appearance_mode("Light")
            self.tema_actual = "Light"
        
    def listar_estudiantes(self):
        from views.viewTkinter.viewEstudiante.listarEstudiantes import ListarEstudiantes
        listar_estudiantes = ListarEstudiantes(self.db, tema_actual=self.tema_actual)
        listar_estudiantes.root.mainloop()
        
    def registrar_estudiante(self):
        from views.viewTkinter.viewEstudiante.registrarEstudiante import RegistrarEstudiante
        registrar_estudiante = RegistrarEstudiante(self.db, tema_actual=self.tema_actual)
        registrar_estudiante.root.mainloop()
        
    def actualizar_estudiante(self):
        from views.viewTkinter.viewEstudiante.actualizarEstudiante import ActualizarEstudiante
        actualizar_estudiante = ActualizarEstudiante(self.db, tema_actual=self.tema_actual)
        actualizar_estudiante.root.mainloop()

    def eliminar_estudiante(self):
        from views.viewTkinter.viewEstudiante.eliminarEstudiante import EliminarEstudiante
        eliminar_estudiante = EliminarEstudiante(self.db, tema_actual=self.tema_actual)
        eliminar_estudiante.root.mainloop()
        
        
        
        
        
        
        
        
    
         
