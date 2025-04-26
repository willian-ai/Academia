import customtkinter as ctk
from tkinter import ttk, messagebox # Importar ttk para crear tablas y messagebox para mostrar mensajes
from controllers.estudiante_controller import EstudianteController
from mysql.connector import IntegrityError

class EliminarEstudiante:
    def __init__(self, db = None, tema_actual = "System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Eliminar Estudiante")
        self.estudiante_controller = EstudianteController(db)

        # Configuracion de la ventana
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana   
        ancho_ventana = int(ancho_pantalla * 0.4)
        alto_ventana = int(alto_pantalla * 0.4)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo_ventana = ctk.CTkLabel(self.root, text="Eliminar Estudiante", font=ctk.CTkFont(size=20, weight="bold"))
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

        # Botones para eliminar estudiante
        self.btn_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar", command=self.eliminar_estudiante)
        self.btn_eliminar.pack(side="left", padx=10)

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
                print(f"Error al cargar los datos de la tabla: {e}")
    
    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        # Crear una ventana de mensaje personalizado
        ventana_mensaje = ctk.CTkToplevel(self.root)
        ventana_mensaje.title(titulo)
        ventana_mensaje.geometry("300x150")
        ventana_mensaje.resizable(False, False)
        
        # Configurar el tema de la ventana  sea modal
        ctk.set_appearance_mode(self.tema_actual)

        # Crear el mensaje
        label_mensaje = ctk.CTkLabel(ventana_mensaje, text=mensaje, font=ctk.CTkFont(size=12))
        label_mensaje.pack(pady=20)

        # Crear boton aceptar
        btn_aceptar = ctk.CTkButton(ventana_mensaje, text="Aceptar", command=ventana_mensaje.destroy)
        btn_aceptar.pack(pady=20)

        # Configurar la ventana para que sea modal# Hacer que la ventana sea modal
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
        
    def eliminar_estudiante(self):
            # Obtener el ID del estudiante seleccionado
        seleccion = self.tabla.selection()
        if not seleccion:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione un estudiante para eliminar", "warning")
            return
            
            # Obtener el ID del estudiante seleccionado
        item = self.tabla.item(seleccion[0])
        id_estudiante = item["values"][0]
        nombre = item["values"][1]
        apellido = item["values"][2]
        correo = item["values"][3]
        telefono = item["values"][4]

            # Mostrar la confirmacion
        confirmacion = self.mostrar_confirmacion(
           "Confirmar Eliminacion", 
            f"¿Está seguro de querer eliminar el estudiante {nombre} {apellido}?")
            
        if confirmacion:
            try:
                self.estudiante_controller.eliminar_estudiante(id_estudiante)
                self.mostrar_mensaje("Eliminacion Exitosa", f"El estudiante {nombre} {apellido} ha sido eliminado correctamente")
                self.cargar_datos_tabla()
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al eliminar el estudiante: {str(e)}", "error")
            
    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        MenuPrincipal = MenuPrincipal(db = self.db, tema_actual = self.tema_actual)
        MenuPrincipal.root.mainloop()
                
                
            
            


