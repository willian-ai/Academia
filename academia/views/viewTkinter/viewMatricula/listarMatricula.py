import customtkinter as ctk
from tkinter import ttk
from controllers.matricula_controller import MatriculaController
from mysql.connector import IntegrityError

class ListarMatriculas:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.root = ctk.CTk()
        self.tema_actual = tema_actual
        self.root.title("Listar Matrículas")
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
        self.titulo = ctk.CTkLabel(self.root, text="Listar Matrículas", font=("Arial", 20, "bold"))
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
    
    def regresar_menu_principal(self):
        from views.viewTkinter.viewMatricula.menuMatricula import MenuMatricula
        self.root.destroy()
        menu_matricula = MenuMatricula(db=self.db, tema_actual=self.tema_actual)
        menu_matricula.root.mainloop() 