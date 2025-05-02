import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.matricula_controller import MatriculaController
from mysql.connector import IntegrityError
from datetime import datetime

class ActualizarMatricula:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Actualizar Matrícula")
        self.controller = MatriculaController(db)
        
        # Configuración de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        
        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuración de restricciones de la ventana
        self.root.resizable(False, False)
        
        # Título de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Actualizar Matrícula", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=10)
        
        # Frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Crear el Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "ID Estudiante", "ID Curso", "Fecha Matrícula"), 
                                 show="headings")
        self.tabla.pack(expand=True, fill="both")
        
        # Configurar las columnas
        self.tabla.heading("ID", text="ID Matrícula")
        self.tabla.heading("ID Estudiante", text="ID Estudiante")
        self.tabla.heading("ID Curso", text="ID Curso")
        self.tabla.heading("Fecha Matrícula", text="Fecha Matrícula")
        
        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=100)
        self.tabla.column("ID Estudiante", width=150)
        self.tabla.column("ID Curso", width=150)
        self.tabla.column("Fecha Matrícula", width=200)
        
         # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)
        
        # Botón para actualizar
        self.btn_actualizar = ctk.CTkButton(self.frame_botones, text="Actualizar", 
                                          command=self.actualizar_matricula)
        self.btn_actualizar.pack(side="left", padx=5)
        
        # Botón para regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", 
                                         command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=5)
        
        # Cargar los datos de la tabla
        self.cargar_datos_tabla()
        
    def cargar_datos_tabla(self):
        try:
            # Obtener los datos de la tabla
            matriculas = self.controller.listar_matriculas()
            
            # Limpiar la tabla antes de cargar los datos
            for row in self.tabla.get_children():
                self.tabla.delete(row)
            
            # Insertar los datos en la tabla
            for matricula in matriculas:
                self.tabla.insert("", "end", values=(
                    matricula.id_matricula,
                    matricula.id_estudiante,
                    matricula.id_curso,
                    matricula.fecha_matricula
                ))
        except IntegrityError as e:
            print(f"Error al cargar los datos de la tabla: {e}")
    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        ventana_mensaje = ctk.CTkToplevel(self.root)
        ventana_mensaje.title(titulo)
        ventana_mensaje.geometry("300x150")
        ventana_mensaje.resizable(False, False)

        ctk.set_appearance_mode(self.tema_actual)

        label_mensaje = ctk.CTkLabel(ventana_mensaje, text=mensaje, font=("Arial", 12))
        label_mensaje.pack(pady=20)

        btn_aceptar = ctk.CTkButton(ventana_mensaje, text="Aceptar", command=ventana_mensaje.destroy)
        btn_aceptar.pack(pady=10)

        ventana_mensaje.transient(self.root)
        ventana_mensaje.grab_set()
        self.root.wait_window(ventana_mensaje)
        
    def mostrar_confirmacion(self, titulo, mensaje):
        ventana_confirmacion = ctk.CTkToplevel(self.root)
        ventana_confirmacion.title(titulo)
        ventana_confirmacion.geometry("300x150")
        ventana_confirmacion.resizable(False, False)

        ctk.root.set_appearance_mode(self.tema_actual)
        respuesta = [False]

        label_mensaje = ctk.CTkLabel(ventana_confirmacion, text=mensaje, font=("Arial", 12))
        label_mensaje.pack(pady=20)

        # Crear frame para los botones
        frame_botones = ctk.CTkFrame(ventana_confirmacion)
        frame_botones.pack(pady=10)

        # Crear botones
        btn_si = ctk.CTkButton(frame_botones, text="Si", command=lambda: 
            [respuesta.__setitem__(0, True), ventana_confirmacion.destroy()], width=100)
        btn_si.pack(side="left", padx=5)

        btn_no = ctk.CTkButton(frame_botones, text="No", command=ventana_confirmacion.destroy, width=100)
        btn_no.pack(side="left", padx=5)

        # Hacer que la ventana sea modal
        ventana_confirmacion.transient(self.root)
        ventana_confirmacion.grab_set()
        self.root.wait_window(ventana_confirmacion)

        return respuesta[0]

    def actualizar_matricula(self):
        # obtener horario seleccionado
        seleccion = self.tabla.selection()       
        if not seleccion:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione una matricula para actualizar", "warning")
            return
        # Obtener los datos de la matricula seleccionada
        item = self.tabla.item(seleccion[0])
        id_matricula = item["values"][0]
        id_estudiante = item["values"][1]
        id_curso = item["values"][2]
        fecha_matricula = item["values"][3]
        
        # Crear ventana de actualizacion
        ventana_actualizacion = ctk.CTkToplevel(self.root)
        ventana_actualizacion.title("Actualizar Matricula")
        ventana_actualizacion.geometry("300x400")
        ventana_actualizacion.resizable(False, False)
        
        # Configurar el tema de la ventana  
        ctk.set_appearance_mode(self.tema_actual)
        
        # Crear campos de entrada
        frame_campos = ctk.CTkFrame(ventana_actualizacion)
        frame_campos.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Campo para el ID del estudiante
        label_id_estudiante = ctk.CTkLabel(frame_campos, text="ID del Estudiante:")
        label_id_estudiante.pack(pady=5)
        
        entry_id_estudiante = ctk.CTkEntry(frame_campos)
        entry_id_estudiante.insert(0, id_estudiante)
        entry_id_estudiante.pack(pady=5)
        
        # Campo para el ID del curso
        label_id_curso = ctk.CTkLabel(frame_campos, text="ID del Curso:")
        label_id_curso.pack(pady=5)
        
        entry_id_curso = ctk.CTkEntry(frame_campos)
        entry_id_curso.insert(0, id_curso)
        entry_id_curso.pack(pady=5)
        
        # Campo para la fecha de matricula
        label_fecha_matricula = ctk.CTkLabel(frame_campos, text="Fecha de Matricula:")
        label_fecha_matricula.pack(pady=5)
        
        entry_fecha_matricula = ctk.CTkEntry(frame_campos)
        entry_fecha_matricula.insert(0, fecha_matricula)
        entry_fecha_matricula.pack(pady=5)
        
        # frame para los botones
        frame_botones = ctk.CTkFrame(ventana_actualizacion)
        frame_botones.pack(pady=10)
        
        # Boton para guardar los cambios
        btn_guardar = ctk.CTkButton(frame_botones, text="Guardar", command=lambda: self.guardar_cambios(id_matricula, ventana_actualizacion), width=100)
        btn_guardar.pack(side="left", padx=5)
        
        # Boton para cancelar los cambios
        btn_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_actualizacion.destroy, width=100)
        btn_cancelar.pack(side="left", padx=5)
        
        # Hacer que la ventana sea modal
        ventana_actualizacion.transient(self.root)
        ventana_actualizacion.grab_set()
        self.root.wait_window(ventana_actualizacion)
        
    def guardar_cambios(self, id_matricula, ventana):
        # Obtener los nuevos valores
        nuevo_id_estudiante = self.entry_id_estudiante.get()
        nuevo_id_curso = self.entry_id_curso.get()
        nuevo_fecha_matricula = self.entry_fecha_matricula.get()
        
        # Validar campos
        if not nuevo_id_estudiante or not nuevo_id_curso or not nuevo_fecha_matricula:
            self.mostrar_mensaje("Error", "Por favor complete todos los campos", "error")
            return
        # Validar que los IDs sean números
        if not nuevo_id_estudiante.isdigit() or not nuevo_id_curso.isdigit():
            self.mostrar_mensaje("Error", "Los IDs deben ser números", "error")
            return
        # Validar formato de fecha
        try:
            datetime.strptime(nuevo_fecha_matricula, "%Y-%m-%d")
        except ValueError:
            self.mostrar_mensaje("Error", "El formato de fecha debe ser YYYY-MM-DD", "error")
            return
        
        # Mostrar confirmacion
        confirmacion = self.mostrar_confirmacion("Confirmar Cambios", 
                                                 "¿Está seguro de querer guardar los cambios?")
        if confirmacion:
            try:
                nuevo_id_estudiante = int(nuevo_id_estudiante)
                nuevo_id_curso = int(nuevo_id_curso)
                
                self.controller.actualizar_matricula(
                    id_matricula = id_matricula,
                    estudiante_id = nuevo_id_estudiante, 
                    curso_id = nuevo_id_curso, 
                    fecha_matricula = nuevo_fecha_matricula
                    )
                
                self.mostrar_mensaje("Éxito", "Matricula actualizada correctamente", "info")
                self.cargar_datos_tabla()
                ventana.destroy()
            except ValueError as e:
                self.mostrar_mensaje("Error", f"El ID debe ser un número", "error")
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al actualizar la matricula: {str(e)}", "error")
        
       
        
    def regresar_menu_principal(self):
        from views.viewTkinter.viewMatricula.menuMatricula import MenuMatricula
        self.root.destroy()
        menu_matricula = MenuMatricula(db=self.db, tema_actual=self.tema_actual)
        menu_matricula.root.mainloop() 