import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.curso_controller import CursoController
from mysql.connector import IntegrityError

class ActualizarCurso:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Actualizar Curso")
        self.curso_controller = CursoController(db)

        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.8)
        alto_ventana = int(alto_pantalla * 0.8)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Actualizar Curso", font=ctk.CTkFont(size=20, weight="bold"))
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

        # Botón para actualizar
        self.btn_actualizar = ctk.CTkButton(self.frame_botones, text="Actualizar", command=self.actualizar_curso)
        self.btn_actualizar.pack(side="left", padx=10)

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
                self.tabla.insert("", "end", values=(
                    curso.id_curso, 
                    curso.nombre, 
                    curso.descripcion, 
                    curso.duracion_hrs, 
                    curso.id_profesor))

        except IntegrityError as e:
            print(f"Error al cargar los datos de la tabla: {e}")

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        ventana_mensaje = ctk.CTkTopLevel()
        ventana_mensaje.title(titulo)
        ventana_mensaje.geometry("300x150")
        ventana_mensaje.resizable(False, False)

        ctk.set_appearance_mode(self.tema_actual)

        label_mensaje = ctk.CTkLabel(ventana_mensaje, text=mensaje, font=("Arial", 12))
        label_mensaje.pack(pady=20)

        # Crear boton Aceptar
        btn_aceptar = ctk.CTkButton(ventana_mensaje, text="Aceptar", command=ventana_mensaje.destroy)
        btn_aceptar.pack(pady=10)

        # Hacer que la ventana sea modal
        ventana_mensaje.transient(self.root)
        ventana_mensaje.grab_set()
        self.root.wait_window(ventana_mensaje)

    def mostrar_confirmacion(self, titulo, mensaje):
        # Crear una ventana de confirmación personalizada
        ventana_confirmacion = ctk.CTkTopLevel()
        ventana_confirmacion.title(titulo)
        ventana_confirmacion.geometry("350x150")
        ventana_confirmacion.resizable(False, False)

        ctk.set_appearance_mode(self.tema_actual)
        respuesta = [False]
        label_mensaje = ctk.CTkLabel(ventana_confirmacion, text=mensaje, font=("Arial", 12))
        label_mensaje.pack(pady=20)

        # Crear botones
        btn_si = ctk.CTkButton(ventana_confirmacion, text="Si", command=lambda: [respuesta.__setitem__(0, True), ventana_confirmacion.destroy()])
        btn_si.pack(side="left", padx=10)

        btn_no = ctk.CTkButton(ventana_confirmacion, text="No", command= ventana_confirmacion.destroy)
        btn_no.pack(side="left", padx=10)
        # Hacer que la ventana sea modal
        ventana_confirmacion.transient(self.root)
        ventana_confirmacion.grab_set()
        self.root.wait_window(ventana_confirmacion)

        return respuesta[0]

        

    def actualizar_curso(self):
        # Obtener el curso seleccionado
        seleccion = self.tabla.selection()
        if not seleccion:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione un curso para actualizar", "warning")
            return

        # Obtener los datos del curso seleccionado
        item = self.tabla.item(seleccion[0])
        id_curso = item["values"][0]
        nombre_actual = item["values"][1]
        descripcion_actual = item["values"][2]
        duracion_actual = item["values"][3]
        id_profesor_actual = item["values"][4]

        # Crear ventana de actualización
        ventana_actualizacion = ctk.CTk()
        ventana_actualizacion.title("Actualizar Curso")
        ventana_actualizacion.geometry("400x450")
        ventana_actualizacion.resizable(False, False)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(self.tema_actual)
        # Crear campos de entrada
        frame_campos = ctk.CTkFrame(ventana_actualizacion)
        frame_campos.pack(pady=20, padx=20, fill="both", expand=True)

        # Campo para el nombre
        label_nombre = ctk.CTkLabel(frame_campos, text="Nombre: ")     
        label_nombre.pack(pady=5)

        self.entry_nombre = ctk.CTkEntry(frame_campos)
        self.entry_nombre.insert(0, nombre_actual)
        self.entry_nombre.pack(pady=5)

        # Campo para la descripción
        label_descripcion = ctk.CTkLabel(frame_campos, text="Descripción: ")
        label_descripcion.pack(pady=5)


        self.entry_descripcion = ctk.CTkEntry(frame_campos)
        self.entry_descripcion.insert(0, descripcion_actual)
        self.entry_descripcion.pack(pady=5)

        # Campo para la duración
        label_duracion = ctk.CTkLabel(frame_campos, text="Duración: ")
        label_duracion.pack(pady=5)

        self.entry_duracion = ctk.CTkEntry(frame_campos)
        self.entry_duracion.insert(0, duracion_actual)
        self.entry_duracion.pack(pady=5)

        # Campo para el ID del profesor
        label_id_profesor = ctk.CTkLabel(frame_campos, text="ID Profesor: ")
        label_id_profesor.pack(pady=5)

        self.entry_id_profesor = ctk.CTkEntry(frame_campos)
        self.entry_id_profesor.insert(0, id_profesor_actual)
        self.entry_id_profesor.pack(pady=5)

        # Frame para los botones
        frame_botones = ctk.CTkFrame(ventana_actualizacion)
        frame_botones.pack(pady=20)

        # Botón para guardar cambios
        btn_guardar = ctk.CTkButton(frame_botones, text="Guardar Cambios", 
                                  command=lambda: self.guardar_cambios(id_curso, ventana_actualizacion))
        btn_guardar.pack(side="left", padx=5)

        #Hacer que la ventana sea modal
        ventana_actualizacion.transient(self.root)
        ventana_actualizacion.grab_set()
        self.root.wait_window(ventana_actualizacion)

       

    def guardar_cambios(self, id_curso, ventana_actualizacion):
        # Obtener los nuevos valores
        nuevo_nombre = self.entry_nombre.get()
        nueva_descripcion = self.entry_descripcion.get()
        nueva_duracion = self.entry_duracion.get()
        nuevo_id_profesor = self.entry_id_profesor.get()

        # Validar campos
        if not nuevo_nombre or not nueva_descripcion or not nueva_duracion or not nuevo_id_profesor:
            self.mostrar_mensaje("Error", "Por favor complete todos los campos", "error")
            return

        try:
            int(nueva_duracion)
            int(nuevo_id_profesor)
        except ValueError:
            self.mostrar_mensaje("Error", "La duración y el ID del profesor deben ser números", "error")
            return

        confirmacion = self.mostrar_confirmacion("Confirmar Actualización", "¿Está seguro de querer actualizar los datos del curso?")
        if confirmacion:
            try:
                self.curso_controller.actualizar_curso(id_curso, nuevo_nombre, nueva_descripcion, nueva_duracion, nuevo_id_profesor)
                self.mostrar_mensaje("Éxito", "Los datos del curso se han actualizado correctamente", "success")
                self.cargar_datos_tabla()
                ventana_actualizacion.destroy()
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al actualizar los datos del curso: {e}", "error")


    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop() 

    