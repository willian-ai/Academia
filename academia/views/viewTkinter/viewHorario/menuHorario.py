import customtkinter as ctk

class MenuHorario:
    def __init__(self, db, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Gestión de Horarios")
        ctk.set_appearance_mode(tema_actual)

        # Configuracion de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_principal)

        # Obtener el ancho y alto de la pantalla    
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.2)
        alto_ventana = int(alto_pantalla * 0.45)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menú Horario", font=("Helvetica", 16))
        self.titulo.pack(pady=10)
        
        # Boton para cambiar el tema
        self.tema_actual = tema_actual
        self.boton_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.boton_cambiar_tema.pack(pady=10)   

        # Boton para listar horarios
        self.boton_listar_horarios = ctk.CTkButton(self.root, text="Listar Horarios", command=self.listar_horarios)
        self.boton_listar_horarios.pack(pady=10)

        # Boton para registrar horario
        self.boton_registrar_horario = ctk.CTkButton(self.root, text="Registrar Horario", command=self.registrar_horario)
        self.boton_registrar_horario.pack(pady=10)
        
        # Boton para actualizar horario
        self.boton_actualizar_horario = ctk.CTkButton(self.root, text="Actualizar Horario", command=self.actualizar_horario)
        self.boton_actualizar_horario.pack(pady=10)

        # Boton para eliminar horario
        self.boton_eliminar_horario = ctk.CTkButton(self.root, text="Eliminar Horario", command=self.eliminar_horario)
        self.boton_eliminar_horario.pack(pady=10)
        
        # Boton para regresar al menu principal
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()
        
    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"
    
    def listar_horarios(self):
        from views.viewTkinter.viewHorario.listarHorario import ListarHorarios
        listar_horarios = ListarHorarios(db = self.db, tema_actual = self.tema_actual)
        listar_horarios.root.mainloop()

    def registrar_horario(self):
        from views.viewTkinter.viewHorario.registrarHorario import RegistrarHorario 
        registrar_horario = RegistrarHorario(db = self.db, tema_actual = self.tema_actual)
        registrar_horario.root.mainloop()

    def actualizar_horario(self):
        from views.viewTkinter.viewHorario.actualizarHorario import ActualizarHorario
        actualizar_horario = ActualizarHorario(db = self.db, tema_actual = self.tema_actual)
        actualizar_horario.root.mainloop()

    def eliminar_horario(self):
        from views.viewTkinter.viewHorario.eliminarHorario import EliminarHorario
        eliminar_horario = EliminarHorario(db = self.db, tema_actual = self.tema_actual)
        eliminar_horario.root.mainloop()



