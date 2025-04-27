import customtkinter as ctk
from tkinter import ttk
from controllers.profesor_controller import ProfesorController
from mysql.connector import IntegrityError

class ListarProfesores:
    def __init__(self, db = None, tema_actual = "System"):
        self.db = db
        self.root = ctk.CTk()
        self.root.title("Listar Profesores")
        self.profesor_controller = ProfesorController(db)

        # Configurar el tema de la ventana
        ctk.set_appearance_mode(tema_actual)
        ctk.set_default_color_theme("green")

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.8)
        alto_ventana = int(alto_pantalla * 0.8)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")

        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Listar Profesores", font=("Helvetica", 20))
        self.titulo.pack(pady=20)

        # Crear el frame principal
        self.tabla = ctk.CTkFrame(self.root)
        self.tabla.pack(padx=40, pady=10, fill="both", expand=True)


        # Crear  la tabla usando treeview   
        self.tabla = ttk.Treeview(self.tabla, columns=("ID", "Nombre", "Apellido", "Email", "Telefono", "Especialidad"), show="headings")
        self.tabla.pack(padx=20, fill="both", expand=True)

        # Configurar el estilo de la tabla
        self.tabla.heading("ID", text="ID Profesor")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Email", text="Email")
        self.tabla.heading("Telefono", text="Telefono")
        self.tabla.heading("Especialidad", text="Especialidad")

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=150)
        self.tabla.column("Nombre", width=250)
        self.tabla.column("Apellido", width=100)
        self.tabla.column("Email", width=300)
        self.tabla.column("Telefono", width=200)
        self.tabla.column("Especialidad", width=250)

        # Crear frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(padx=40, pady=20)

        # Crear  boton para regresar al menu principal  
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=10)
        
        # Cargar los dtos de la tabla
        self.cargar_datos_tabla()

    def cargar_datos_tabla(self):
        try:
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
            print(f"Error al cargar los datos de la tabla: {e}")
        
    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.db, self.tema_actual)
        menu_principal.root.mainloop()

    
        
        
        
        
        
        
    