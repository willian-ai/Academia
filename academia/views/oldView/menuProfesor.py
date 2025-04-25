from controllers.profersor_controller import ProfesorController
from mysql.connector import IntegrityError

def menu_profesor(db):
    profesor_controller = ProfesorController(db)

    while True:
        print("Bienvenido al sistema de gestion de profesores")
        print("1. Registrar profesor")
        print("2. Listar profesores")
        print("3. Obtener profesor por ID")
        print("4. Actualizar profesor")
        print("5. Eliminar profesor")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            registrar_profesor(profesor_controller)
        elif opcion == "2":
            listar_profesores(profesor_controller)
        elif opcion == "3":
            obtener_profesor_id(profesor_controller)
        elif opcion == "4":
            actualizar_profesor(profesor_controller)
        elif opcion == "5":
            eliminar_profesor(profesor_controller)
        elif opcion == "6":
            print("Saliendo del programa del sistema de profesores.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def registrar_profesor(profesor_controller):
    print("=========== Registrar Profesor ==========")
    nombre = input("Ingrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    correo = input("Ingrese el correo del profesor: ")
    telefono = input("Ingrese el telefono del profesor: ")
    especialidad = input("Ingrese la especialidad del profesor: ")

    try:
        profesor_controller.registrar_profesor(nombre, apellido, correo, telefono, especialidad)
        print("Profesor registrado correctamente.")
    except IntegrityError as e:
        print(f"Error al registrar el profesor: {e}")

def listar_profesores(profesor_controller):
    print("=========== Listar Profesores ==========")
    try:
        profesores = profesor_controller.listar_profesores()
        if profesores:
            print("ID\tNombre\tApellido\tCorreo\tTelefono\tEspecialidad")
            for profesor in profesores:
                print(f"{profesor.id_profesor}\t{profesor.nombre}\t{profesor.apellido}\t{profesor.correo}\t{profesor.telefono}\t{profesor.especialidad}")
        else:
            print("No hay profesores registrados.")
    except Exception as e:
        print(f"Error al listar los profesores: {e}")

def obtener_profesor_id(profesor_controller):
    print("=========== Obtener Profesor por ID ==========")
    id_profesor = input("Ingrese el ID del profesor: ")
    try:
        profesor = profesor_controller.obtener_profesor_id(id_profesor)
        if profesor:
            print(f"ID: {profesor.id_profesor}")
            print(f"Nombre: {profesor.nombre}")
            print(f"Apellido: {profesor.apellido}")
            print(f"Correo: {profesor.correo}")
            print(f"Telefono: {profesor.telefono}")
            print(f"Especialidad: {profesor.especialidad}")
        else:   
            print("No hay profesores registrados.")
    except Exception as e:
        print(f"Error al obtener el profesor: {e}")

def actualizar_profesor(profesor_controller):
    print("=========== Actualizar Profesor ==========") 
    id_profesor = input("Ingrese el ID del profesor a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del profesor: ")
    apellido = input("Ingrese el nuevo apellido del profesor: ")
    correo = input("Ingrese el nuevo correo del profesor: ")
    telefono = input("Ingrese el nuevo telefono del profesor: ")
    especialidad = input("Ingrese la nueva especialidad del profesor: ")

    try:
        profesor_controller.actualizar_profesor(id_profesor, nombre, apellido, correo, telefono, especialidad)
        print("Profesor actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el profesor: {e}")
        
def eliminar_profesor(profesor_controller):
    print("=========== Eliminar Profesor ==========")
    id_profesor = input("Ingrese el ID del profesor a eliminar: ")
    try:
        profesor_controller.eliminar_profesor(id_profesor)
        print("Profesor eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el profesor: {e}")

    




