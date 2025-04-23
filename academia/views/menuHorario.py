from controllers.horario_controller import HorarioController
from mysql.connector import IntegrityError

def menu_horario(db):
    horario_controller = HorarioController(db)

    while True:
        print("Bienvenido al menu de gestion de horarios")
        print("1. Registrar horario")
        print("2. Listar horarios")
        print("3. Obtener horario por ID")
        print("4. Actualizar horario")
        print("5. Eliminar horario")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_horario(horario_controller)
        elif opcion == "2":
            listar_horarios(horario_controller)
        elif opcion == "3":
            obtener_horario_por_id(horario_controller)
        elif opcion == "4":
            actualizar_horario(horario_controller)
        elif opcion == "5":
            eliminar_horario(horario_controller)
        elif opcion == "6":
            print("Saliendo del menu de gestion de horarios")
            break
        else:
            print("Opcion invalida. Por favor, seleccione una opcion valida.")

def registrar_horario(horario_controller):
    print("============= Registrar horario =============")
    dia = input("Ingrese el dia de la semana (Lunes, Martes, etc.): ")
    hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
    hora_fin = input("Ingrese la hora de fin (HH:MM): ")
    curso_id = int(input("Ingrese el ID del curso: "))

    try:
        horario_controller.registrar_horario(dia, hora_inicio, hora_fin, curso_id)
        print("Horario registrado correctamente")
    except IntegrityError as e:
        print(f"Error al registrar el horario: {str(e)}")
  

def listar_horarios(horario_controller):
    print("============= Listar horarios =============")
    horarios = horario_controller.listar_horarios()
    if horarios:
        for horario in horarios:
            print(f"ID: {horario.id_horario}")
            print(f"Dia de la semana: {horario.dia_semana}")
            print(f"Hora inicio: {horario.hora_inicio}")
            print(f"Hora fin: {horario.hora_fin}")
            print(f"ID del curso: {horario.id_curso}")
            print(f"Nombre del curso: {horario.nombre_curso}")
            print("===========================================")
    else:
        print("No se encontraron horarios registrados")

def obtener_horario_por_id(horario_controller):
    print("============= Obtener horario por ID =============")
    id_horario = int(input("Ingrese el ID del horario: "))

    try:
        horario = horario_controller.obtener_horario_por_id(id_horario)
        if horario:
            print(f"ID: {horario.id_horario}")
            print(f"Dia de la semana: {horario.dia_semana}")
            print(f"Hora inicio: {horario.hora_inicio}")
            print(f"Hora fin: {horario.hora_fin}")
            print(f"ID del curso: {horario.id_curso}")
            print(f"Nombre del curso: {horario.nombre_curso}")  
            print("===========================================")
        else:
            print("No se encontró ningún horario con ese ID")
    except Exception as e:
        print(f"Error al obtener el horario: {str(e)}")

def actualizar_horario(horario_controller):
    print("============= Actualizar horario =============")
    id_horario = int(input("Ingrese el ID del horario a actualizar: "))
    dia_semana = input("Ingrese el nuevo dia de la semana (Lunes, Martes, etc.): ")
    hora_inicio = input("Ingrese la nueva hora de inicio (HH:MM): ")
    hora_fin = input("Ingrese la nueva hora de fin (HH:MM): ")
    curso_id = int(input("Ingrese el nuevo ID del curso: "))

    try:
        horario_controller.actualizar_horario(id_horario, dia_semana, hora_inicio, hora_fin, curso_id)
        print("Horario actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar el horario: {str(e)}")

def eliminar_horario(horario_controller):
    print("============= Eliminar horario =============")
    id_horario = int(input("Ingrese el ID del horario a eliminar: "))
    
    try:
        horario_controller.eliminar_horario(id_horario)
        print("Horario eliminado correctamente")
    except Exception as e:
        print(f"Error al eliminar el horario: {str(e)}")    

            
            



