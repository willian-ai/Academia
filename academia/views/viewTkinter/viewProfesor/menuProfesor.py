import customtkinter as ctk


class MenuProfesor:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Menu Profesor")

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        # Configurar cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_principal)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.2)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.root.resizable(False, False)

        
        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menu Profesor", font=("Arial", 16))
        self.titulo.pack(pady=10)
        
            # Boton para listar profesores
        self.btn_listar_profesores = ctk.CTkButton(self.root, text="Listar Profesores", 
                                                  command=self.listar_profesores)
        self.btn_listar_profesores.pack(pady=10)

        # Boton para registrar un nuevo profesor
        self.btn_registrar_profesor = ctk.CTkButton(self.root, text="Registrar Profesor", 
                                                   command=self.registrar_profesor)
        self.btn_registrar_profesor.pack(pady=10)

        # Boton para actualizar un profesor
        self.btn_actualizar_profesor = ctk.CTkButton(self.root, text="Actualizar Profesor", 
                                                    command=self.actualizar_profesor, height=40)
        self.btn_actualizar_profesor.pack(pady=10)

        # Boton para eliminar un profesor
        self.btn_eliminar_profesor = ctk.CTkButton(self.root, text="Eliminar Profesor", 
                                                  command=self.eliminar_profesor)
        self.btn_eliminar_profesor.pack(pady=10)

        # Boton para cambiar el tema de la ventana
        self.btn_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", 
                                             command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(pady=10)

        # Boton para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.root, text="Regresar", 
                                         command=self.regresar_menu_principal)
        self.btn_regresar.pack(pady=10)

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()

    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"

    def listar_profesores(self):
        from views.viewTkinter.viewProfesor.listarProfesor import ListarProfesores
        listar_profesor = ListarProfesores(db=self.db, tema_actual=self.tema_actual)
        listar_profesor.root.mainloop()

    def registrar_profesor(self):
        from views.viewTkinter.viewProfesor.registrarProfesor import RegistrarProfesor
        registrar_profesor = RegistrarProfesor(db=self.db, tema_actual=self.tema_actual)
        registrar_profesor.root.mainloop()

    def actualizar_profesor(self):
        from views.viewTkinter.viewProfesor.actualizarProfesor import ActualizarProfesor
        actualizar_profesor = ActualizarProfesor(db=self.db, tema_actual=self.tema_actual)
        actualizar_profesor.root.mainloop() 

    def eliminar_profesor(self):
        from views.viewTkinter.viewProfesor.eliminarProfesor import EliminarProfesor
        eliminar_profesor = EliminarProfesor(db=self.db, tema_actual=self.tema_actual)
        eliminar_profesor.root.mainloop()

        
        
        
        
        
        

        
        

