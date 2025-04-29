import customtkinter as ctk
from tkinter import ttk, messagebox
from controllers.horario_controller import HorarioController
from mysql.connector import IntegrityError
import re
class ActualizarHorario:
    def __init__(self, db=None, tema_actual="System"):
        self.db = db
        self.tema_actual = tema_actual
        self.root = ctk.CTk()
        self.root.title("Actualizar Horario")
        self.controller = HorarioController(db)

        # Configuracion de la ventana
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
        self.titulo = ctk.CTkLabel(self.root, text="Actualizar Horario", font=("Arial", 20, "bold"))
        self.titulo.pack(pady=10)
        
        # Crear un frame para la tabla
        self.frame_tabla = ctk.CTkFrame(self.root)
        self.frame_tabla.pack(pady=10)
        
        # Crear el Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=("ID", "Curso ID", "Día", "Hora Inicio", "Hora Fin"), show="headings")
        self.tabla.pack(expand=True, fill="both")
        
        # Configurar las columnas
        self.tabla.heading("ID", text="ID Horario")
        self.tabla.heading("Curso ID", text="Curso ID")
        self.tabla.heading("Día", text="Día")
        self.tabla.heading("Hora Inicio", text="Hora Inicio")
        self.tabla.heading("Hora Fin", text="Hora Fin")
        

        # Ajustar el ancho de las columnas
        self.tabla.column("ID", width=100)
        self.tabla.column("Curso ID", width=150)
        self.tabla.column("Día", width=150)
        self.tabla.column("Hora Inicio", width=150)
        self.tabla.column("Hora Fin", width=150)

        # Frame para los botones
        self.frame_botones = ctk.CTkFrame(self.root)
        self.frame_botones.pack(pady=10)

        # Botón para actualizar
        self.btn_actualizar = ctk.CTkButton(self.frame_botones, text="Actualizar", command=self.actualizar_horario)
        self.btn_actualizar.pack(side="left", padx=5)

        # Botón para regresar
        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Regresar", command=self.regresar_menu_principal)
        self.btn_regresar.pack(side="left", padx=5)

        # Cargar los datos de la tabla
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

        ventana_mensaje.transient(self.root)
        ventana_mensaje.grab_set()
        self.root.wait_window(ventana_mensaje)

    def mostrar_confirmacion(self, titulo, mensaje):
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

    def actualizar_horario(self):
        # Obtener el horario seleccionado   
        seleccion = self.tabla.selection()
        if not seleccion:
            self.mostrar_mensaje("Advertencia", "Por favor seleccione un horario para actualizar", "warning")
            return

        # Obtener los datos del horario seleccionado    
        item = self.tabla.item(seleccion[0])
        id_horario = item["values"][0]
        curso_id = item["values"][1]
        dia_semana = item["values"][2]
        hora_inicio = item["values"][3]
        hora_fin = item["values"][4]

        # Crear ventana de actualización
        ventana_actualizacion = ctk.CTkToplevel(self.root)
        ventana_actualizacion.title("Actualizar Horario")
        ventana_actualizacion.geometry("300x500")
        ventana_actualizacion.resizable(False, False)

        # Configurar el tema de la ventana  
        ctk.set_appearance_mode(self.tema_actual)

        # Crear campos de entrada
        frame_campos = ctk.CTkFrame(ventana_actualizacion)
        frame_campos.pack(pady=20, padx=20, fill="both", expand=True)

        # Campo para el ID del curso
        label_curso_id = ctk.CTkLabel(frame_campos, text="ID del Curso:")
        label_curso_id.pack(pady=5)

        self.entry_curso_id = ctk.CTkEntry(frame_campos)
        self.entry_curso_id.insert(0, curso_id)
        self.entry_curso_id.pack(pady=5)

        # Campo para el día de la semana
        label_dia_semana = ctk.CTkLabel(frame_campos, text="Día de la Semana:")
        label_dia_semana.pack(pady=5)

        self.entry_dia_semana = ctk.CTkEntry(frame_campos)
        self.entry_dia_semana.insert(0, dia_semana)
        self.entry_dia_semana.pack(pady=5)

        # Campo para la hora de inicio
        label_hora_inicio = ctk.CTkLabel(frame_campos, text="Hora de Inicio:")
        label_hora_inicio.pack(pady=5)

        self.entry_hora_inicio = ctk.CTkEntry(frame_campos)
        self.entry_hora_inicio.insert(0, hora_inicio)
        self.entry_hora_inicio.pack(pady=5)

        # Campo para la hora de fin
        label_hora_fin = ctk.CTkLabel(frame_campos, text="Hora de Fin:")
        label_hora_fin.pack(pady=5)

        self.entry_hora_fin = ctk.CTkEntry(frame_campos)
        self.entry_hora_fin.insert(0, hora_fin)
        self.entry_hora_fin.pack(pady=5)

        # Frame para los botones
        frame_botones = ctk.CTkFrame(ventana_actualizacion)
        frame_botones.pack(pady=20)

        # Botón para guardar cambios
        btn_guardar = ctk.CTkButton(frame_botones, text="Guardar Cambios", 
                                    command=lambda: self.guardar_cambios(id_horario, ventana_actualizacion))
        btn_guardar.pack(side="left", padx=5)

        # Botón para cancelar
        btn_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_actualizacion.destroy)
        btn_cancelar.pack(side="left", padx=5)

        # Hacer que la ventana sea modal
        ventana_actualizacion.transient(self.root)
        ventana_actualizacion.grab_set()
        self.root.wait_window(ventana_actualizacion)

    def guardar_cambios(self, id_horario, ventana):
        # Obtener los nuevos valores
        nuevo_curso_id = self.entry_curso_id.get()
        nuevo_dia_semana = self.entry_dia_semana.get()
        nuevo_hora_inicio = self.entry_hora_inicio.get()
        nuevo_hora_fin = self.entry_hora_fin.get()
        
        # Validar campos
        if not nuevo_curso_id or not nuevo_dia_semana or not nuevo_hora_inicio or not nuevo_hora_fin:
            self.mostrar_mensaje("Error", "Todos los campos son requeridos", "error")
            return
        
        # Validar formato de hora (HH:MM:SS)
        hora_regex = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
        if not re.match(hora_regex, nuevo_hora_inicio) or not re.match(hora_regex, nuevo_hora_fin):
            self.mostrar_mensaje("Error", "El formato de hora debe ser HH:MM:SS (24 horas)", "error")
            return

        # Validar que la hora de fin sea mayor que la hora de inicio
        hora_inicio = int(nuevo_hora_inicio.replace(':', ''))
        hora_fin = int(nuevo_hora_fin.replace(':', ''))
        if hora_fin <= hora_inicio:
            self.mostrar_mensaje("Error", "La hora de fin debe ser mayor que la hora de inicio", "error")
            return  
        
        # Mostrar confirmación
        confirmacion = self.mostrar_confirmacion("Confirmar Actualización",
                                               "¿Estás seguro de querer actualizar los datos del horario?")
        
        if confirmacion:
            # Actualizar el horario
            try:
                # Convertir el ID del curso a entero
                nuevo_curso_id = int(nuevo_curso_id)
                # Llamar al controlador con los parámetros en el orden correcto
                self.controller.actualizar_horario(
                    id_horario=id_horario,
                    id_curso=nuevo_curso_id,
                    dia=nuevo_dia_semana,
                    hora_inicio=nuevo_hora_inicio,
                    hora_fin=nuevo_hora_fin
                )
                self.mostrar_mensaje("Éxito", "Los datos del horario se han actualizado correctamente", "info")
                self.cargar_datos_tabla()
                ventana.destroy()
            except ValueError:
                self.mostrar_mensaje("Error", "El ID del curso debe ser un número", "error")
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al actualizar el horario: {str(e)}", "error")
        
        
    def regresar_menu_principal(self):
        from views.viewTkinter.menuPrincipal import MenuPrincipal
        self.root.destroy()
        menu_principal = MenuPrincipal(db=self.db, tema_actual=self.tema_actual)
        menu_principal.root.mainloop()
        
        
        
        
        

        
       