import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.horario_controller import HorarioController
from mysql.connector import IntegrityError


class ListarHorarios:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Listar Horarios")
        self.horario_controller = HorarioController(db)

        # Configuracion de la ventana
        ctk.set_appearance_mode(tema_actual)
        
        # Configuracion de la ventana
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Listar Horarios", font=("Helvetica", 16))
        self.titulo.pack(pady=10)

        # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=20)

        # Crear el Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Curso ID", "Día", "Hora Inicio", "Hora Fin"), show="headings")
        self.tabla.pack(expand=True, fill="both")

        # Configurar columnas
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Curso ID", text="Curso ID")
        self.tabla.heading("Día", text="Día")
        self.tabla.heading("Hora Inicio", text="Hora Inicio")
        self.tabla.heading("Hora Fin", text="Hora Fin")
        
        # Ajustar anchos de columna
        self.tabla.column("ID", width=100)
        self.tabla.column("Curso ID", width=100)
        self.tabla.column("Día", width=150)
        self.tabla.column("Hora Inicio", width=150)
        self.tabla.column("Hora Fin", width=150)
       
        # Botón para regresar
        self.boton_regresar = ctk.CTkButton(self.root, text="Regresar", command=self.regresar_menu_principal)
        self.boton_regresar.pack(pady=10)

        self.cargar_datos_tabla()

    def cargar_datos_tabla(self):
        try:
            # Obtener los datos de la tabla
            horarios = self.horario_controller.listar_horarios()
            # Limpiar la tabla antes de cargar los datos
            for row in self.tabla.get_children():
                self.tabla.delete(row)

            # Insertar los datos en la tabla
            for horario in horarios:
                self.tabla.insert("", "end", values=(
                    horario.id_horario,
                    horario.id_curso,
                    horario.dia_semana,
                    horario.hora_inicio,
                    horario.hora_fin
                ))
        except IntegrityError as e:
            print(f"Error al cargar los datos de la tabla: {e}")

            
    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()

    