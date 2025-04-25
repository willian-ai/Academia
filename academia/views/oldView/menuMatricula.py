from controllers.matricula_controller import MatriculaController
from mysql.connector import IntegrityError

def menu_matricula(db):
    matricula_controller = MatriculaController(db)
    while True:
        print("Bienvenido al sistema de gestion de Matriculas")
        print("1. Registrar Matricula")
        print("2. Listar Matriculas")
        print("3. Obtener Matricula por ID")
        print("4. Actualizar Matricula")
        print("5. Eliminar Matricula")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_matricula(matricula_controller)
        elif opcion == "2":
            listar_matriculas(matricula_controller)
        elif opcion == "3":
            obtener_matricula_por_id(matricula_controller)
        elif opcion == "4":
            actualizar_matricula(matricula_controller)
        elif opcion == "5":
            eliminar_matricula(matricula_controller)
        elif opcion == "6":
            print("Saliendo del sistema de gestion de Matriculas")
            break
        else:
            print("Opcion invalida. Por favor, seleccione una opcion valida.")
        



def registrar_matricula(matricula_controller):
    print("=========== Registrar Matricula ===========")
    estudiante_id = int(input("Ingrese el ID del estudiante: "))
    curso_id = int(input("Ingrese el ID del curso: "))
    fecha_matricula = input("Ingrese la fecha de matricula (YYYY-MM-DD): ")
    
    try:
        matricula_controller.registrar_matricula(estudiante_id, curso_id, fecha_matricula)
        print("Matricula registrada correctamente.")
    except IntegrityError as e:
        print(f"Error al registrar la matricula: {e}")

def listar_matriculas(matricula_controller):
    print("=========== Listar Matriculas ===========")
    matriculas = matricula_controller.listar_matriculas()
    
    for matricula in matriculas:
            print(f"ID matricula: {matricula.id_matricula}")
            print(f"Fecha matricula: {matricula.fecha_matricula}")
            print(f"ID estudiante: {matricula.id_estudiante}")
            print(f"ID curso: {matricula.id_curso}")
            print("================================================ ")

def obtener_matricula_por_id(matricula_controller):
    print("=========== Obtener Matricula por ID ===========")
    id_matricula = int(input("Ingrese el ID de la matricula: "))
    
    matricula = matricula_controller.obtener_matricula_por_id(id_matricula)
    
    if matricula:
        print(f"ID matricula: {matricula.id_matricula}")
        print(f"Fecha matricula: {matricula.fecha_matricula}")
        print(f"ID estudiante: {matricula.id_estudiante}")
        print(f"ID curso: {matricula.id_curso}")
        print("================================================ ")
    else:
        print("No se encontro la matricula con el ID proporcionado.")

def actualizar_matricula(matricula_controller):
    print("=========== Actualizar Matricula ===========")
    id_matricula = int(input("Ingrese el ID de la matricula a actualizar: "))
    estudiante_id = int(input("Ingrese el nuevo ID del estudiante: "))
    curso_id = int(input("Ingrese el nuevo ID del curso: "))
    fecha_matricula = input("Ingrese la nueva fecha de matricula (YYYY-MM-DD): ")
    
    try:
        matricula_controller.actualizar_matricula(id_matricula, estudiante_id, curso_id, fecha_matricula)
        print("Matricula actualizada correctamente.")       
    except IntegrityError as e:
        print(f"Error al actualizar la matricula: {e}")

def eliminar_matricula(matricula_controller):
    print("=========== Eliminar Matricula ===========")
    id_matricula = int(input("Ingrese el ID de la matricula a eliminar: "))

    try:
        matricula_controller.eliminar_matricula(id_matricula)
        print("Matricula eliminada correctamente.")
    except IntegrityError as e:
        print(f"Error al eliminar la matricula: {e}")

        
