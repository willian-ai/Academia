from controllers.curso_controller import CursoController
from controllers.profersor_controller import ProfesorController
from mysql.connector import IntegrityError

def menu_curso(db):
    curso_controller = CursoController(db)
    profesor_controller = ProfesorController(db)
    while True:
        print("Bienvenido al sistema de gestion de cursos")
        print("1. Registrar Curso")
        print("2. Listar Cursos")
        print("3. Obtener Curso por ID")
        print("4. Actualizar Curso")
        print("5. Eliminar Curso")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_curso(curso_controller)
        elif opcion == "2":
            listar_cursos(curso_controller)
        elif opcion == "3":
            obtener_curso_por_id(curso_controller)
        elif opcion == "4":
            actualizar_curso(curso_controller)
        elif opcion == "5":
            eliminar_curso(curso_controller)
        elif opcion == "6":
            print("Saliendo del sistema de gestion de cursos ....")
            break
        else:
            print("Opcion invalida, por favor ingrese una opcion valida")


def registrar_curso(curso_controller):
    print("============== Registrar Curso ==============")
    nombre = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripcion del curso: ")
    duracion_hrs = input("Ingrese la duracion del curso en horas: ")
    id_profesor = input("Ingrese el ID del profesor que imparte el curso: ")
    
    try:    
        curso_controller.registrar_curso(nombre, descripcion, duracion_hrs, id_profesor)
        print("Curso registrado correctamente")
    except IntegrityError as e:
        print(f"Error al registrar el curso: {str(e)}")

def listar_cursos(curso_controller):
    print("============== Listar Cursos ==============")
    cursos = curso_controller.listar_cursos()
    if cursos:
        for curso in cursos:
            print(f"ID: {curso.id_curso}")
            print(f"Nombre: {curso.nombre}")
            print(f"Descripcion: {curso.descripcion}")
            print(f"Duracion: {curso.duracion_hrs}")
            print(f"ID Profesor: {curso.id_profesor}")
            print(f"Profesor: {curso.profesor_nombre}")
            print("================================================")
    else:
        print("No hay cursos registrados.")

def obtener_curso_por_id(curso_controller):
    print("============== Obtener Curso por ID ==============")
    id_curso = input("Ingrese el ID del curso a obtener: ")
    curso = curso_controller.obtener_curso_por_id(id_curso)
    if curso:
        print(f"ID: {curso.id_curso}")
        print(f"Nombre: {curso.nombre}")
        print(f"Descripcion: {curso.descripcion}")
        print(f"Duracion: {curso.duracion_hrs}")
        print(f"ID Profesor: {curso.id_profesor}")
        print(f"Profesor: {curso.profesor_nombre}")
    else:
        print("No se encontro el curso")

def actualizar_curso(curso_controller):
    print("============== Actualizar Curso ==============")
    id_curso = input("Ingrese el ID del curso a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del curso: ")
    descripcion = input("Ingrese la nueva descripcion del curso: ")
    duracion_hrs = input("Ingrese la nueva duracion del curso en horas: ")
    id_profesor = input("Ingrese el nuevo ID del profesor que imparte el curso: ")
    
    try:
        curso_controller.actualizar_curso(id_curso, nombre, descripcion, duracion_hrs, id_profesor)
        print("Curso actualizado correctamente")
    except Exception as e:
        print(f"Error al actualizar el curso: {str(e)}")

def eliminar_curso(curso_controller):
    print("============== Eliminar Curso ==============")
    id_curso = input("Ingrese el ID del curso a eliminar: ")
    try:
        curso_controller.eliminar_curso(id_curso)
        print("Curso eliminado correctamente")
    except Exception as e:
        print(f"Error al eliminar el curso: {str(e)}")
