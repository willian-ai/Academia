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
        
        # Frame para los campos de actualización
        self.frame_campos = ctk.CTkFrame(self.root)
        self.frame_campos.pack(pady=10, padx=20, fill="x")
        
        # Campo para el ID de la matrícula
        self.label_id = ctk.CTkLabel(self.frame_campos, text="ID de la Matrícula a Actualizar:")
        self.label_id.pack(pady=5)
        
        self.entry_id = ctk.CTkEntry(self.frame_campos)
        self.entry_id.pack(pady=5, fill="x")
        
        # Campo para el ID del estudiante
        self.label_estudiante = ctk.CTkLabel(self.frame_campos, text="Nuevo ID del Estudiante:")
        self.label_estudiante.pack(pady=5)
        
        self.entry_estudiante = ctk.CTkEntry(self.frame_campos)
        self.entry_estudiante.pack(pady=5, fill="x")
        
        # Campo para el ID del curso
        self.label_curso = ctk.CTkLabel(self.frame_campos, text="Nuevo ID del Curso:")
        self.label_curso.pack(pady=5)
        
        self.entry_curso = ctk.CTkEntry(self.frame_campos)
        self.entry_curso.pack(pady=5, fill="x")
        
        # Campo para la fecha de matrícula
        self.label_fecha = ctk.CTkLabel(self.frame_campos, text="Nueva Fecha de Matrícula (YYYY-MM-DD):")
        self.label_fecha.pack(pady=5)
        
        self.entry_fecha = ctk.CTkEntry(self.frame_campos)
        self.entry_fecha.pack(pady=5, fill="x")
        
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
        
        # Configurar evento de selección en la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_matricula)
    
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
    
    def seleccionar_matricula(self, event):
        # Obtener la fila seleccionada
        seleccion = self.tabla.selection()
        if seleccion:
            # Obtener los valores de la fila seleccionada
            valores = self.tabla.item(seleccion[0])["values"]
            # Llenar los campos con los valores seleccionados
            self.entry_id.delete(0, "end")
            self.entry_id.insert(0, str(valores[0]))
            self.entry_estudiante.delete(0, "end")
            self.entry_estudiante.insert(0, str(valores[1]))
            self.entry_curso.delete(0, "end")
            self.entry_curso.insert(0, str(valores[2]))
            self.entry_fecha.delete(0, "end")
            self.entry_fecha.insert(0, str(valores[3]))
    
    def validar_campos(self):
        # Validar que todos los campos estén llenos
        if not self.entry_id.get() or not self.entry_estudiante.get() or not self.entry_curso.get() or not self.entry_fecha.get():
            self.mostrar_mensaje("Error", "Todos los campos son requeridos", "error")
            return False
        
        # Validar que los IDs sean números
        try:
            int(self.entry_id.get())
            int(self.entry_estudiante.get())
            int(self.entry_curso.get())
        except ValueError:
            self.mostrar_mensaje("Error", "Los IDs deben ser números", "error")
            return False
        
        # Validar formato de fecha
        try:
            datetime.strptime(self.entry_fecha.get(), '%Y-%m-%d')
        except ValueError:
            self.mostrar_mensaje("Error", "El formato de fecha debe ser YYYY-MM-DD", "error")
            return False
        
        return True
    
    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje)
        else:
            messagebox.showinfo(titulo, mensaje)
    
    def actualizar_matricula(self):
        if not self.validar_campos():
            return
        
        try:
            # Obtener los valores de los campos
            id_matricula = int(self.entry_id.get())
            id_estudiante = int(self.entry_estudiante.get())
            id_curso = int(self.entry_curso.get())
            fecha_matricula = self.entry_fecha.get()
            
            # Actualizar la matrícula
            self.controller.actualizar_matricula(id_matricula, id_estudiante, id_curso, fecha_matricula)
            
            # Mostrar mensaje de éxito
            self.mostrar_mensaje("Éxito", "Matrícula actualizada correctamente")
            
            # Actualizar la tabla
            self.cargar_datos_tabla()
            
            # Limpiar los campos
            self.entry_id.delete(0, "end")
            self.entry_estudiante.delete(0, "end")
            self.entry_curso.delete(0, "end")
            self.entry_fecha.delete(0, "end")
            
        except IntegrityError as e:
            self.mostrar_mensaje("Error", "Error al actualizar la matrícula: " + str(e), "error")
        except Exception as e:
            self.mostrar_mensaje("Error", "Error al actualizar la matrícula: " + str(e), "error")
    
    def regresar_menu_principal(self):
        from views.viewTkinter.viewMatricula.menuMatricula import MenuMatricula
        self.root.destroy()
        menu_matricula = MenuMatricula(db=self.db, tema_actual=self.tema_actual)
        menu_matricula.root.mainloop() 