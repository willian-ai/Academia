import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.curso_controller import CursoController
from mysql.connector import IntegrityError

class EliminarCurso:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Eliminar Curso")
        self.curso_controller = CursoController(db)

        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.4)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Eliminar Curso", font=ctk.CTkFont(size=20, weight="bold"))
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
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Descripción", width=200)
        self.tabla.column("Duración", width=100)
        self.tabla.column("ID Profesor", width=100)

        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)

        # Botón para eliminar
        self.btn_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar", command=self.eliminar_curso)
        self.btn_eliminar.pack(side="left", padx=10)

        # Botón para regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=10)

        # Cargar los datos de la tabla
        self.cargar_datos_tabla()

    def cargar_datos_tabla(self):
        try:
            # Obtener los datos de la tabla
            cursos = self.curso_controller.listar_cursos()

            # Limpiar la tabla antes de cargar los datos
            for row in self.tabla.get_children():
                self.tabla.delete(row)

            # Insertar los datos en la tabla
            for curso in cursos:
                self.tabla.insert("", "end", values=(curso.id_curso, curso.nombre, curso.descripcion, curso.duracion_hrs, curso.id_profesor))

        except IntegrityError as e:
            print(f"Error al cargar los datos de la tabla: {e}")

    def eliminar_curso(self):
        # Obtener el curso seleccionado
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor seleccione un curso para eliminar")
            return

        # Obtener los datos del curso seleccionado
        item = self.tabla.item(seleccion[0])
        id_curso = item["values"][0]
        nombre = item["values"][1]

        # Mostrar confirmación
        if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de querer eliminar el curso {nombre}?"):
            try:
                # Eliminar el curso
                self.curso_controller.eliminar_curso(id_curso)
                messagebox.showinfo("Éxito", "El curso ha sido eliminado correctamente")
                self.cargar_datos_tabla()
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar el curso: {e}")

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop() 