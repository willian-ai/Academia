import customtkinter as ctk


class MenuMatricula:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Gestión de Matrículas")
        
        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Configuracion de cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.regresar_menu_principal)
        
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
        self.titulo = ctk.CTkLabel(self.root, text="Gestión de Matrículas", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=20)

        # Boton para cambiar tema
        self.boton_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.boton_cambiar_tema.pack(pady=10)

        # Boton para listar matrículas
        self.boton_listar_matriculas = ctk.CTkButton(self.root, text="Listar Matrículas", command=self.listar_matriculas)
        self.boton_listar_matriculas.pack(pady=10)

        # Boton para registrar matrícula
        self.boton_registrar_matricula = ctk.CTkButton(self.root, text="Registrar Matrícula", command=self.registrar_matricula)
        self.boton_registrar_matricula.pack(pady=10)

        # Boton para actualizar matrícula
        self.boton_actualizar_matricula = ctk.CTkButton(self.root, text="Actualizar Matrícula", command=self.actualizar_matricula)
        self.boton_actualizar_matricula.pack(pady=10)

        # Boton para eliminar matrícula
        self.boton_eliminar_matricula = ctk.CTkButton(self.root, text="Eliminar Matrícula", command=self.eliminar_matricula)
        self.boton_eliminar_matricula.pack(pady=10)

        # Boton para regresar al menu principal
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

    def cambiar_tema(self):
        if self.tema_actual == "Light":
            ctk.set_appearance_mode("Dark")
            self.tema_actual = "Dark"
        else:
            ctk.set_appearance_mode("Light")
            self.tema_actual = "Light"

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()

    def listar_matriculas(self):
        from views.viewTkinter.viewMatricula.listarMatricula import ListarMatriculas
        listar_matriculas = ListarMatriculas(db=self.db, tema_actual=self.tema_actual)
        listar_matriculas.root.mainloop()

    def registrar_matricula(self):
        from views.viewTkinter.viewMatricula.registrarMatricula import RegistrarMatricula
        registrar_matricula = RegistrarMatricula(db=self.db, tema_actual=self.tema_actual)
        registrar_matricula.root.mainloop()

    def actualizar_matricula(self):
        from views.viewTkinter.viewMatricula.actualizarMatricula import ActualizarMatricula
        actualizar_matricula = ActualizarMatricula(db=self.db, tema_actual=self.tema_actual)
        actualizar_matricula.root.mainloop()

    def eliminar_matricula(self):
        from views.viewTkinter.viewMatricula.eliminarMatricula import EliminarMatricula
        eliminar_matricula = EliminarMatricula(db=self.db, tema_actual=self.tema_actual)
        eliminar_matricula.root.mainloop()



