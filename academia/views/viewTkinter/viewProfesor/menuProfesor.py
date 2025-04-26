import customtkinter as ctk
import platform
from tkinter import ttk
from controllers.profesor_controller import ProfesorController
from mysql.connector import IntegrityError

class MenuProfesor:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Menu Profesor")
        
        #Configuracion del tema
        ctk.set_appearance_mode(tema_actual)
        ctk.set_default_color_theme("green")

        # Configuracion del cierre de la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        #Dimensiones de la ventana
        ancho_ventana = self.root.winfo_screenwidth() 
        alto_ventana = self.root.winfo_screenheight()

        # Asignar tamaño de la ventana

        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.root.state("zoomed")

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Menu Profesor", font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=20)

       # Crear un frame principal para la tabla y los botones
        self.frame_principal = ctk.CTkFrame(self.root)
        self.frame_principal.pack(pady=20, padx=40, fill="both", expand=True)

       # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.frame_principal)
        self.frame_tabla.pack(side="left", fill="both", expand=True, padx=(0, 20))

        # Crear tabla usando treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Nombre", "Apellido", "Email", "Telefono", "Especialidad"), show="headings")
        self.tabla.pack(expand=True, fill="both", padx=20)
        self.tabla.heading("ID", text="ID Profesor")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Email", text="Email")
        self.tabla.heading("Telefono", text="Telefono")
        self.tabla.heading("Especialidad", text="Especialidad")

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=150)
        self.tabla.column("Nombre", width=250)
        self.tabla.column("Apellido", width=250)
        self.tabla.column("Email", width=300)
        self.tabla.column("Telefono", width=200)
        self.tabla.column("Especialidad", width=250)

        # crear frame para botones verticales
        self.frame_botones = ctk.CTkFrame(self.frame_principal, width=250)
        self.frame_botones.pack(side="right", fill="both", expand=True, padx=(0, 20))
        self.frame_botones.pack_propagate(False) # Evitar que el frame se ajuste al contenido
        
        # Boton para registrar profesor
        self.boton_registrar = ctk.CTkButton(self.frame_botones, text="Registrar Profesor", command=self.registrar_profesor)
        self.boton_registrar.pack(fill="x", padx=20, pady=20)
       
       # Boton para actualizar profesor
        self.boton_actualizar = ctk.CTkButton(self.frame_botones, text="Actualizar Profesor", command=self.actualizar_profesor)
        self.boton_actualizar.pack(fill="x", padx=20, pady=20)
       
       # Boton para eliminar profesor
        self.boton_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar Profesor", command=self.eliminar_profesor)
        self.boton_eliminar.pack(fill="x", padx=20, pady=20)    

        # Boton para cambiar tema
        self.boton_cambiar_tema = ctk.CTkButton(self.frame_botones, text="Cambiar Tema", command=self.cambiar_tema)
        self.boton_cambiar_tema.pack(fill="x", padx=20, pady=20)

        # Boton para cerrar sesion
        self.boton_cerrar_sesion = ctk.CTkButton(self.frame_botones, text="Cerrar Sesion", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.pack(fill="x", padx=20, pady=20)   

        # Cambiar los datos de la tabla
        self.cargar_datos_tabla()

        # Agregar espacio vertical
        self.espacio_vertical = ctk.CTkFrame(self.frame_principal, text="")
        self.espacio_vertical.pack(pady=20)

        # Crear un frame para el boton regresar
        self.frame_boton = ctk.CTkFrame(self.root)
        self.frame_boton.pack(pady=20, padx=20, fill="x")

        # Boton para regresar
        self.boton_regresar = ctk.CTkButton(self.frame_boton, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(fill="left", padx=20)

    def cargar_datos_tabla(self):
        try:
            profesores = ProfesorController.obtener_profesores()
            for row in self.tabla.get_children():
                self.tabla.delete(row)

            for profesor in profesores:
                self.tabla.insert("", "end", values=(
                    profesor.id_profesor,
                    profesor.nombre, 
                    profesor.apellido, 
                    profesor.email, 
                    profesor.telefono, 
                    profesor.especialidad 
                    ))
        except IntegrityError as e:
            print(f"Error al cargar los datos de la tabla: {e}")

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db = self.db, tema_actual = self.tema_actual)
        menu_principal.root.mainloop()
            
       
        
