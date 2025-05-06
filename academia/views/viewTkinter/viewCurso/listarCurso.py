import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.curso_controller import CursoController
from mysql.connector import IntegrityError

class ListarCursos:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.tema_actual = tema_actual
        self.root.title("Listar Cursos")
        self.curso_controller = CursoController(db)

        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Listar Cursos", font=("Helvetica", 16))
        self.titulo_ventana.pack(pady=20)

        # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=20)

        # Crear el Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Descripción", "Duración", "ID Profesor"), show="headings")
        self.tabla.pack(expand=True, fill="both")

        # Configurar las columnas
        self.tabla.heading("ID", text="ID Curso")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Descripción", text="Descripción")
        self.tabla.heading("Duración", text="Duración (horas)")
        self.tabla.heading("ID Profesor", text="ID Profesor")

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=100)
        self.tabla.column("Nombre", width=200)
        self.tabla.column("Descripción", width=250)
        self.tabla.column("Duración", width=100)
        self.tabla.column("ID Profesor", width=80)

        # Cargar los datos de la tabla
        self.cargar_datos_tabla()

        # Botón para regresar
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

    def cargar_datos_tabla(self):
        try:
            # Obtener los datos de la tabla
            cursos = self.curso_controller.listar_cursos()

            # Limpiar la tabla antes de cargar los datos
            for row in self.tabla.get_children():
                self.tabla.delete(row)

            # Insertar los datos en la tabla
            for curso in cursos:
                self.tabla.insert("", "end", values=(
                    curso.id_curso, 
                    curso.nombre, 
                    curso.descripcion, 
                    curso.duracion_hrs, 
                    curso.id_profesor))

        except IntegrityError as e:
            print(f"Error al cargar los datos de la tabla: {e}")

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop() 