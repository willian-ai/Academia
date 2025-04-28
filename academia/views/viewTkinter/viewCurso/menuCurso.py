import customtkinter as ctk

class MenuCurso:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Menú Curso")

        # Configuración de la ventana
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
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Menú Curso", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo_ventana.pack(pady=10)

        # Boton para cambiar el tema
        self.tema_actual = tema_actual
        self.boton_cambiar_tema = ctk.CTkButton(self.root, text="Cambiar Tema", command=self.cambiar_tema)
        self.boton_cambiar_tema.pack(pady=10)

        # Boton para listar cursos
        self.boton_listar_cursos = ctk.CTkButton(self.root, text="Listar Cursos", command=self.listar_cursos)
        self.boton_listar_cursos.pack(pady=10)

        # Boton para registrar curso
        self.boton_registrar_curso = ctk.CTkButton(self.root, text="Registrar Curso", command=self.registrar_curso)
        self.boton_registrar_curso.pack(pady=10)

        # Boton para actualizar curso
        self.boton_actualizar_curso = ctk.CTkButton(self.root, text="Actualizar Curso", command=self.actualizar_curso)
        self.boton_actualizar_curso.pack(pady=10)

        # Boton para eliminar curso
        self.boton_eliminar_curso = ctk.CTkButton(self.root, text="Eliminar Curso", command=self.eliminar_curso)
        self.boton_eliminar_curso.pack(pady=10)

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

    def listar_cursos(self):
        from views.viewTkinter.viewCurso.listarCurso import ListarCursos
        listar_cursos = ListarCursos(self.db, tema_actual=self.tema_actual)
        listar_cursos.root.mainloop()

    def registrar_curso(self):
        from views.viewTkinter.viewCurso.registrarCurso import RegistrarCurso
        registrar_curso = RegistrarCurso(self.db, tema_actual=self.tema_actual)
        registrar_curso.root.mainloop()

    def actualizar_curso(self):
        from views.viewTkinter.viewCurso.actualizarCurso import ActualizarCurso
        actualizar_curso = ActualizarCurso(self.db, tema_actual=self.tema_actual)
        actualizar_curso.root.mainloop()

    def eliminar_curso(self):
        from views.viewTkinter.viewCurso.eliminarCurso import EliminarCurso
        eliminar_curso = EliminarCurso(self.db, tema_actual=self.tema_actual)
        eliminar_curso.root.mainloop()
