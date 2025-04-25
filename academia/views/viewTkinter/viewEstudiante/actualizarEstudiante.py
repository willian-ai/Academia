import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.controllerEstudiante import EstudianteController
from mysql.connector import IntegrityError
import re

class ActualizarEstudiante:
    def __init__(self, db = None, tema_actual = "System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Actualizar Estudiante")
        self.estudiante_controller = EstudianteController(db)

        # Configuracion de la ventana
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
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Actualizar Estudiante", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo_ventana.pack(pady=20)

        # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=20)

        # Crear el Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Correo", "Telefono"), show="headings")    
        self.tabla.pack(expand=True, fill="both")

        # Configurar las columnas
        self.tabla.heading("ID", text="ID Estudiante")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Telefono", text="Telefono")

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=100)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Apellido", width=150)
        self.tabla.column("Correo", width=200)
        self.tabla.column("Telefono", width=120)

        # Cargar los datos de la tabla
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=20)

        # Botones para actualizar estudiante
        self.btn_actualizar = ctk.CTkButton(self.frame_botones, text="Actualizar", command=self.actualizar_estudiante)
        self.btn_actualizar.pack(side="left", padx=10)

        # Botones para regresar al menu principal
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=10)

        def cargar_datos_tabla(self):
            try:
                # Obtener los datos de la tabla
                estudiantes = self.estudiante_controller.obtener_todos_estudiantes()

                # Limpiar la tabla antes de cargar los datos
                for row in self.tabla.get_children():
                    self.tabla.delete(row)

                # Insertar los datos en la tabla
                for estudiante in estudiantes:
                    self.tabla.insert("", "end", values=(estudiante.id_estudiante, estudiante.nombre, estudiante.apellido, estudiante.correo, estudiante.telefono))
                    
            except IntegrityError as e:
                messagebox.showerror("Error", f"Error al cargar los datos de la tabla: {e}")

        def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
            # Crear una ventana de mensaje personalizado
            ventana_mensaje = ctk.CTkToplevel(self.root)
            ventana_mensaje.title(titulo)
            ventana_mensaje.geometry("300x150")
            ventana_mensaje.resizable(False, False) 

            # Configurar el tema de la ventana
            ctk.set_appearance_mode(self.tema_actual)

            # Crear el mensaje
            label_mensaje = ctk.CTkLabel(ventana_mensaje, text=mensaje, font=ctk.CTkFont(size=12))
            label_mensaje.pack(pady=20)

            # Crear boton aceptar
            btn_aceptar = ctk.CTkButton(ventana_mensaje, text="Aceptar", command=ventana_mensaje.destroy)
            btn_aceptar.pack(pady=20)

            # Configurar la ventana para que sea modal
            ventana_mensaje.transient(self.root)
            ventana_mensaje.grab_set()
            self.root.wait_window(ventana_mensaje)


        def mostrar_confirmacion(self, titulo, mensaje):
            # Crear una ventana de confirmacion
            ventana_confirmacion = ctk.CTkToplevel(self.root)
            ventana_confirmacion.title(titulo)
            ventana_confirmacion.geometry("300x150")
            ventana_confirmacion.resizable(False, False)    

            # Configurar el tema de la ventana      
            ctk.set_appearance_mode(self.tema_actual)

            # Variable para almacenar la respuesta
            respuesta = [False]

            # Crear el mensaje
            label_mensaje = ctk.CTkLabel(ventana_confirmacion, text=mensaje, font=ctk.CTkFont(size=12))
            label_mensaje.pack(pady=20)

            # Crear frame para los botones
            frame_botones = ctk.CTkFrame(ventana_confirmacion)
            frame_botones.pack(pady=20)

            # Crear boton si
            btn_si = ctk.CTkButton(frame_botones, text="Si", command=lambda: [respuesta.__setitem__(0, True), ventana_confirmacion.destroy()])
            btn_si.pack(side="left", padx=10)

            # Crear boton no
            btn_no = ctk.CTkButton(frame_botones, text="No", command=ventana_confirmacion.destroy)
            btn_no.pack(side="left", padx=10)   

            # Configurar la ventana para que sea modal
            ventana_confirmacion.transient(self.root)
            ventana_confirmacion.grab_set()
            self.root.wait_window(ventana_confirmacion)

            return respuesta[0]
            
        def actualizar_estudiante(self):
            # Obtener el ID del estudiante seleccionado
            seleccion = self.tabla.selection()
            if not seleccion:
                self.mostrar_mensaje("Advertencia", "Por favor seleccione un estudiante para actualizar", "warning")
                return
            
            # Obtener el ID del estudiante seleccionado
            item = self.tabla.item(seleccion[0])
            id_estudiante = item["values"][0]
            nombre = item["values"][1]
            apellido = item["values"][2]
            correo = item["values"][3]
            telefono = item["values"][4]

            # Crear ventana de actualizacion
            ventana_actualizacion = ctk.CTkToplevel(self.root)
            ventana_actualizacion.title("Actualizar Estudiante")
            ventana_actualizacion.geometry("300x200")
            ventana_actualizacion.resizable(False, False)

            # Configurar el tema de la ventana
            ctk.set_appearance_mode(self.tema_actual)

            # Crear el formulario de actualizacion
            frame_campos = ctk.CTkFrame(ventana_actualizacion)
            frame_campos.pack(pady=20, padx=20, expand=True, fill="both")

            # Crear etiquetas y campos de entrada
            lbl_nombre = ctk.CTkLabel(frame_campos, text="Nombre:")
            lbl_nombre.pack(pady=10)
            self.entry_nombre = ctk.CTkEntry(frame_campos)
            self.entry_nombre.insert(0, nombre)
            self.entry_nombre.pack(pady=10)

            # Campo de apellido
            lbl_apellido = ctk.CTkLabel(frame_campos, text="Apellido:")
            lbl_apellido.pack(pady=10)
            self.entry_apellido = ctk.CTkEntry(frame_campos)
            self.entry_apellido.insert(0, apellido)
            self.entry_apellido.pack(pady=10)

            # Campo de correo
            lbl_correo = ctk.CTkLabel(frame_campos, text="Correo:")
            lbl_correo.pack(pady=10)
            self.entry_correo = ctk.CTkEntry(frame_campos)
            self.entry_correo.insert(0, correo)
            self.entry_correo.pack(pady=10)

            # Campo de telefono
            lbl_telefono = ctk.CTkLabel(frame_campos, text="Telefono:")
            lbl_telefono.pack(pady=10)
            self.entry_telefono = ctk.CTkEntry(frame_campos)
            self.entry_telefono.insert(0, telefono)
            self.entry_telefono.pack(pady=10)

            # Frame para los botones
            frame_botones = ctk.CTkFrame(ventana_actualizacion)
            frame_botones.pack(pady=20)

            # Boton para guardar cambios
            btn_guardar = ctk.CTkButton(frame_botones, text="Guardar", command=lambda: self.guardar_cambios(id_estudiante, nombre, apellido, correo, telefono))
            btn_guardar.pack(side="left", padx=10)

            # Boton para cancelar
            btn_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_actualizacion.destroy)
            btn_cancelar.pack(side="left", padx=10)

            # Hacer que la ventana sea modal
            ventana_actualizacion.transient(self.root)
            ventana_actualizacion.grab_set()
            self.root.wait_window(ventana_actualizacion)

        def guardar_cambios(self, id_estudiante,ventana_actualizacion):
            # Obtener los nuevos nombre
            nuevo_nombre = self.entry_nombre.get()
            nuevo_apellido = self.entry_apellido.get()
            nuevo_correo = self.entry_correo.get()
            nuevo_telefono = self.entry_telefono.get()

            # Verificar si los campos estan llenos  
            if not nuevo_nombre or not nuevo_apellido or not nuevo_correo or not nuevo_telefono:
                self.mostrar_mensaje("Advertencia", "Por favor complete todos los campos", "warning")
                return
            
            if not re.match(r"[^@]+@[^@]+\.[^@]+", nuevo_correo):
                self.mostrar_mensaje("Advertencia", "Por favor ingrese un correo valido", "error")
                return
            
           # Mostrar confirmacion
            confirmacion = self.mostrar_confirmacion ("Confirmacion",
                                            "¿Está seguro de querer actualizar los datos del estudiante?")
            if confirmacion:
                try:
                    # Actualizar los datos del estudiante
                    self.estudiante_controller.actualizar_estudiante(id_estudiante, nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_telefono)
                    self.mostrar_mensaje("Exito", "Los datos del estudiante se han actualizado correctamente", "success")
                    self.cargar_datos_tabla()
                    ventana_actualizacion.destroy()
                except Exception as e:
                    self.mostrar_mensaje("Error", f"Error al actualizar los datos del estudiante: {e}", "error")

        def regresar_menu_principal(self):
            from views.viewTkinter.viewEstudiante.menuEstudiante import MenuEstudiante
            self.root.destroy()
            menu_principal = MenuEstudiante(db = self.db, tema_actual=self.tema_actual)
            menu_principal.root.mainloop()
            
            
            
                
            
            
                    
        
        
        
        
        
        
        
        
