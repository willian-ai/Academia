import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.matricula_controller import MatriculaController
from mysql.connector import IntegrityError

class EliminarMatricula:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Eliminar Matrícula")
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
        self.titulo = ctk.CTkLabel(self.root, text="Eliminar Matrícula", font=("Arial", 20, "bold"))
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
        
        # Botón para eliminar
        self.btn_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar", 
                                        command=self.eliminar_matricula)
        self.btn_eliminar.pack(side="left", padx=5)
        
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
    def mostrar_confirmacion(self, titulo, mensaje):
        # Crear una ventana de confirmación personalizada
        ventana_confirmacion = ctk.CTkToplevel(self.root)
        ventana_confirmacion.title(titulo)
        ventana_confirmacion.geometry("350x150")
        ventana_confirmacion.resizable(False, False)

        ctk.set_appearance_mode(self.tema_actual)
        respuesta = [False]
        label_mensaje = ctk.CTkLabel(ventana_confirmacion, text=mensaje, font=("Arial", 12))
        label_mensaje.pack(pady=20)

         # Crear frame para los botones
        frame_botones = ctk.CTkFrame(ventana_confirmacion)
        frame_botones.pack(pady=10)

        btn_si = ctk.CTkButton(frame_botones, text="Si", command=lambda: [respuesta.__setitem__(0, True), ventana_confirmacion.destroy()], width=100)
        btn_si.pack(side="left", padx=5)

        btn_no = ctk.CTkButton(frame_botones, text="No", command=ventana_confirmacion.destroy, width=100)
        btn_no.pack(side="left", padx=5)

        # Hacer que la ventana sea modal
        ventana_confirmacion.transient(self.root)
        ventana_confirmacion.grab_set()
        self.root.wait_window(ventana_confirmacion)

        return respuesta[0]
    
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

        # Hacer que la ventana sea modal
        ventana_mensaje.transient(self.root)
        ventana_mensaje.grab_set()
        self.root.wait_window(ventana_mensaje)

    def eliminar_matricula(self):
        # Obtener la fila seleccionada
        seleccion = self.tabla.selection()
        if not seleccion:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione una matrícula para eliminar", "warning")
            return
        
        # Obtener los datos de la matrícula seleccionada
        item = self.tabla.item(seleccion[0])
        id_matricula = item["values"][0]
        id_estudiante = item["values"][1]
        id_curso = item["values"][2]
        fecha_matricula = item["values"][3]

        # Mostrar dialogo de confirmacion
        confirmacion = self.mostrar_confirmacion("Confirmar Eliminación", 
                                               f"¿Está seguro de querer eliminar la matrícula {id_matricula}?")
        
        if confirmacion:
            try:
                self.controller.eliminar_matricula(id_matricula)
                self.mostrar_mensaje("Éxito", "Matrícula eliminada correctamente", "info")
                self.cargar_datos_tabla()
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al eliminar la matrícula: {str(e)}", "error")
        
    def regresar_menu_principal(self):  
        from views.viewTkinter.viewMatricula.menuMatricula import MenuMatricula
        self.root.destroy()
        menu_matricula = MenuMatricula(db=self.db, tema_actual=self.tema_actual)
        menu_matricula.root.mainloop() 
        
    def seleccionar_matricula(self, event):
        # Obtener la fila seleccionada
        seleccion = self.tabla.selection()
        if seleccion:
            # Obtener los valores de la fila seleccionada
            valores = self.tabla.item(seleccion[0])["values"]
            # Llenar el campo con el ID seleccionado
            self.entry_id.delete(0, "end")
            self.entry_id.insert(0, str(valores[0]))
    
    def validar_campo(self):
        # Validar que el campo ID esté lleno
        if not self.entry_id.get():
            self.mostrar_mensaje("Error", "El ID de la matrícula es requerido", "error")
            return False
        
        # Validar que el ID sea un número
        try:
            int(self.entry_id.get())
        except ValueError:
            self.mostrar_mensaje("Error", "El ID debe ser un número", "error")
            return False
        
        return True
    
    