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
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.6)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.root.resizable(False, False)

        # Crear un frame principal para centrar los elementos
        self.frame_principal = ctk.CTkFrame(self.root)
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.frame_principal, text="Menu Profesor", font=("Helvetica", 24, "bold"))
        self.titulo.pack(pady=20)
        
        # Crear un frame para los botones
        self.frame_botones = ctk.CTkFrame(self.frame_principal)
        self.frame_botones.pack(expand=True, fill="both", padx=20, pady=20)

        # Boton para listar profesores
        self.btn_listar_profesores = ctk.CTkButton(self.frame_botones, text="Listar Profesores", 
                                                  command=self.listar_profesores)
        self.btn_listar_profesores.pack(fill="x", pady=10, padx=20)

        # Boton para registrar un nuevo profesor
        self.btn_registrar_profesor = ctk.CTkButton(self.frame_botones, text="Registrar Profesor", 
                                                   command=self.registrar_profesor)
        self.btn_registrar_profesor.pack(fill="x", pady=10, padx=20)

        # Boton para actualizar un profesor
        self.btn_actualizar_profesor = ctk.CTkButton(self.frame_botones, text="Actualizar Profesor", 
                                                    command=self.actualizar_profesor, height=40)
        self.btn_actualizar_profesor.pack(fill="x", pady=10, padx=20)

        # Boton para eliminar un profesor
        self.btn_eliminar_profesor = ctk.CTkButton(self.frame_botones, text="Eliminar Profesor", 
                                                  command=self.eliminar_profesor)
        self.btn_eliminar_profesor.pack(fill="x", pady=10, padx=20)

        # Boton para cambiar el tema de la ventana
        self.btn_cambiar_tema = ctk.CTkButton(self.frame_botones, text="Cambiar Tema", 
                                             command=self.cambiar_tema)
        self.btn_cambiar_tema.pack(fill="x", pady=10, padx=20)

        # Boton para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", 
                                         command=self.regresar_menu_principal)
        self.btn_regresar.pack(fill="x", pady=10, padx=20)

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

        
        
        
        
        
        

        
        

