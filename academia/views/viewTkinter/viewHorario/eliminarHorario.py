import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.horario_controller import HorarioController
from mysql.connector import IntegrityError


class EliminarHorario:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Eliminar Horario")
        self.controller = HorarioController(db)
       
        # Configuracion de la ventan    a
        ctk.set_appearance_mode(tema_actual)

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Asignar el tamaño de la ventana
        ancho_ventana = int(ancho_pantalla * 0.7)
        alto_ventana = int(alto_pantalla * 0.5)
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}")
        
        # Configuracion de restricciones de la ventana
        self.root.resizable(False, False)

        # Titulo de la ventana
        self.titulo = ctk.CTkLabel(self.root, text="Eliminar Horario", font=("Helvetica", 16))
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
        self.tabla.column("ID", width=50)
        self.tabla.column("Curso ID", width=100)
        self.tabla.column("Día", width=150)
        self.tabla.column("Hora Inicio", width=150)
        self.tabla.column("Hora Fin", width=150)

        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)

        # Botón para eliminar
        self.btn_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar", command=self.eliminar_horario)
        self.btn_eliminar.pack(side="left", padx=10)

        # Botón para regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=10)

        # Cargar datos
        self.cargar_datos_tabla()

    def cargar_datos_tabla(self):
        try:
            # Obtener los datos de la tabla
            horarios = self.controller.listar_horarios()
            
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

        # Crear botones
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

        # Crear boton Aceptar   
        btn_aceptar = ctk.CTkButton(ventana_mensaje, text="Aceptar", command=ventana_mensaje.destroy)
        btn_aceptar.pack(pady=10)

        # Hacer que la ventana sea modal
        ventana_mensaje.transient(self.root)
        ventana_mensaje.grab_set()
        self.root.wait_window(ventana_mensaje)

    def eliminar_horario(self):
        # Obtener el horario seleccionado
        seleccion = self.tabla.selection()
        if not seleccion:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione un horario para eliminar", "warning")
            
            
        # Obtener los datos del horario seleccionado
        item = self.tabla.item(seleccion[0])
        id_horario = item["values"][0]
        curso_id = item["values"][1]
        #dia_semana = item["values"][2]
        #hora_inicio = item["values"][3]
        #hora_fin = item["values"][4]
        
        # Mostrar dialogo de confirmacion
        confirmacion = self.mostrar_confirmacion("Confirmar Eliminación", 
                                               f"¿Está seguro de querer eliminar el horario?")
        
        if confirmacion:
            try:
                self.controller.eliminar_horario(id_horario)
                self.mostrar_mensaje("Éxito", "El horario ha sido eliminado correctamente", "info")
                self.cargar_datos_tabla()
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al eliminar el horario: {str(e)}", "error")

    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(self.tema_actual)
        menu_principal.root.mainloop()

        
        
        
        
        
        
        
        