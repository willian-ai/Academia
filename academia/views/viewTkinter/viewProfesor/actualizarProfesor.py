import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.profesor_controller import ProfesorController
from mysql.connector import IntegrityError
import re

class ActualizarProfesor:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Actualizar Profesor")
        self.profesor_controller = ProfesorController(db)

         # Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
       

        # Configurar el alto y ancho de la ventana
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.6)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Actualizar Profesor", font=("Helvetica", 16))
        self.titulo.pack(pady=10)

        # Crear un frame para la tabla de profesores
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10)

        # Crear tabla usando treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Email", "Telefono", "Especialidad"), show="headings")
        self.tabla.pack(expand=True, fill="both")
        
               
        # Configurar encabezados
        self.tabla.heading("ID", text="ID Profesor")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Email", text="Email")
        self.tabla.heading("Telefono", text="Telefono")
        self.tabla.heading("Especialidad", text="Especialidad")
        
        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=100)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Apellido", width=150)
        self.tabla.column("Email", width=200)
        self.tabla.column("Telefono", width=150)
        self.tabla.column("Especialidad", width=150)

        # Crear un frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)

        # Crear boton para actualizar un profesor
        self.btn_actualizar = ctk.CTkButton(self.frame_botones, text="Actualizar", command=self.actualizar_profesor)
        self.btn_actualizar.pack(side="left", padx=5)

        # Crear boton para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=5)    
        
        # Cargar los datos de los profesores
        self.cargar_profesores()

    def cargar_profesores(self):
        try:
            # Obtener los datos de los profesores
            profesores = self.profesor_controller.listar_profesores()

            for row in self.tabla.get_children():
                self.tabla.delete(row)

            for profesor in profesores:
                self.tabla.insert("", "end", values=(
                    profesor.id_profesor, 
                    profesor.nombre, 
                    profesor.apellido, 
                    profesor.correo, 
                    profesor.telefono, 
                    profesor.especialidad
                ))

        except IntegrityError as e:
            print(f"Error al cargar los profesores: {e}")

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        # Crear una ventana de mensaje
        ventana_mensaje = ctk.CTkToplevel(self.root)
        ventana_mensaje.title(titulo)
        ventana_mensaje.geometry("300x150")
        ventana_mensaje.resizable(False, False)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(self.tema_actual)

        # Crear un frame para el mensaje
        frame_mensaje = ctk.CTkFrame(ventana_mensaje)
        frame_mensaje.pack(pady=10, padx=10, fill="both", expand=True)

        # Crear el mensaje
        label_mensaje = ctk.CTkLabel(frame_mensaje, text=mensaje, font=("Helvetica", 12))
        label_mensaje.pack(pady=10)

        # Crear un botón de aceptar
        btn_aceptar = ctk.CTkButton(frame_mensaje, text="Aceptar", 
                                   command=ventana_mensaje.destroy,
                                   width=100)
        btn_aceptar.pack(pady=10)

        # Hacer que la ventana sea modal
        ventana_mensaje.transient(self.root)
        ventana_mensaje.grab_set()
        self.root.wait_window(ventana_mensaje)
       
    def mostrar_confirmacion(self, titulo, mensaje):
        # Crear una ventana de confirmacion personalizada
        ventana_confirmacion = ctk.CTkToplevel(self.root)
        ventana_confirmacion.title(titulo)
        ventana_confirmacion.geometry("300x150")
        ventana_confirmacion.resizable(False, False)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(self.tema_actual)

        # Variable para almacenar la respuesta
        respuesta = [False]

        # Crear un frame para el mensaje
        frame_mensaje = ctk.CTkFrame(ventana_confirmacion)
        frame_mensaje.pack(pady=10, padx=10, fill="both", expand=True)

        # Crear el mensaje
        label_mensaje = ctk.CTkLabel(frame_mensaje, text=mensaje, font=("Helvetica", 12))
        label_mensaje.pack(pady=10)

        # Crear un frame para los botones
        frame_botones = ctk.CTkFrame(frame_mensaje)
        frame_botones.pack(pady=10)

        # Crear botones si y no
        btn_si = ctk.CTkButton(frame_botones, text="Si", 
                              command=lambda: [respuesta.__setitem__(0, True), ventana_confirmacion.destroy()],
                              width=100)
        btn_si.pack(side="left", padx=10)

        btn_no = ctk.CTkButton(frame_botones, text="No", 
                              command=ventana_confirmacion.destroy,
                              width=100)
        btn_no.pack(side="left", padx=10)

        # Hacer que la ventana sea modal
        ventana_confirmacion.transient(self.root)
        ventana_confirmacion.grab_set()
        self.root.wait_window(ventana_confirmacion)

        return respuesta[0]
    
    def actualizar_profesor(self):
        # Obtener el item seleccionado de la tabla
        seleccion = self.tabla.selection()

        if not seleccion:
            self.mostrar_mensaje("Advertencia", "No se ha seleccionado ningun profesor para actualizar", "warning")
            return
        
        # Obtener los datos del estudiante seleccionado
        item = self.tabla.item(seleccion[0])
        id_profesor = item["values"][0]
        nombre = item["values"][1]
        apellido = item["values"][2]
        email = item["values"][3]
        telefono = item["values"][4]
        especialidad = item["values"][5]

        # Crear una ventana para actualizar los datos del profesor
        ventana_actualizar = ctk.CTkToplevel(self.root)
        ventana_actualizar.title("Actualizar Profesor")
        ventana_actualizar.geometry("300x500")
        ventana_actualizar.resizable(False, False)  

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(self.tema_actual)

        # Crear  campos de entrada
        frame_campos = ctk.CTkFrame(ventana_actualizar)
        frame_campos.pack(pady=10, padx=10, fill="both", expand=True)

        # Campo de entrada para el nombre
        campo_nombre = ctk.CTkLabel(frame_campos, text="Nombre:")
        campo_nombre.pack(pady=5)
        self.entry_nombre = ctk.CTkEntry(frame_campos)
        self.entry_nombre.insert(0, nombre)
        self.entry_nombre.pack(pady=5)

        # Campo de entrada para el apellido 
        campo_apellido = ctk.CTkLabel(frame_campos, text="Apellido:")
        campo_apellido.pack(pady=5)
        self.entry_apellido = ctk.CTkEntry(frame_campos)
        self.entry_apellido.insert(0, apellido)
        self.entry_apellido.pack(pady=5)

        # Campo de entrada para el email
        campo_email = ctk.CTkLabel(frame_campos, text="Email:")
        campo_email.pack(pady=5)
        self.entry_email = ctk.CTkEntry(frame_campos)
        self.entry_email.insert(0, email)
        self.entry_email.pack(pady=5)
        
        # Campo de entrada para el telefono
        campo_telefono = ctk.CTkLabel(frame_campos, text="Telefono:")
        campo_telefono.pack(pady=5)
        self.entry_telefono = ctk.CTkEntry(frame_campos)
        self.entry_telefono.insert(0, telefono)
        self.entry_telefono.pack(pady=5)

        # Campo de entrada para la especialidad
        campo_especialidad = ctk.CTkLabel(frame_campos, text="Especialidad:")
        campo_especialidad.pack(pady=5)
        self.entry_especialidad = ctk.CTkEntry(frame_campos)
        self.entry_especialidad.insert(0, especialidad)
        self.entry_especialidad.pack(pady=5)

        # Crear frame para los botones
        frame_botones = ctk.CTkFrame(ventana_actualizar)
        frame_botones.pack(pady=20)

        # Crear boton para guardar los cambios
        btn_guardar = ctk.CTkButton(frame_botones, text="Guardar", 
                                    command=lambda: self.guardar_actualizacion(id_profesor, ventana_actualizar))
        btn_guardar.pack(side="left", padx=5)

        # Crear boton para cancelar los cambios
        btn_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_actualizar.destroy)
        btn_cancelar.pack(side="left", padx=5)

        # Hacer que la ventana sea modal
        ventana_actualizar.transient(self.root)
        ventana_actualizar.grab_set()
        self.root.wait_window(ventana_actualizar)

    def guardar_actualizacion(self, id_profesor, ventana):
        # Obtener los datos de los campos de entrada
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()
        especialidad = self.entry_especialidad.get()

        # Validar campos de entrada
        if not nombre or not apellido or not email or not telefono or not especialidad:
            self.mostrar_mensaje("Error", "Todos los campos son requeridos", "error")
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.mostrar_mensaje("Error", "El formato del email no es válido", "error")
            return

        # Mostrar confirmación
        confirmacion = self.mostrar_confirmacion("Confirmar Actualización",
                                               "¿Estás seguro de querer actualizar los datos del profesor?")
        
        if confirmacion:
            try:
                 # Actualizar los datos del profesor
                self.profesor_controller.actualizar_profesor(id_profesor, nombre, apellido, email, telefono, especialidad)
                self.mostrar_mensaje("Éxito", "Los datos del profesor se han actualizado correctamente", "success")
                self.cargar_profesores()
                ventana.destroy()
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al actualizar los datos del profesor: {str(e)}", "error")

    def regresar_menu_principal(self):
        from views.viewTkinter.viewProfesor.menuProfesor import MenuProfesor
        self.root.destroy()
        menu_profesor = MenuProfesor(db=self.db, tema_actual=self.tema_actual)
        menu_profesor.root.mainloop()

        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                
