from controllers.estudiante_controller import EstudianteController
from mysql.connector import IntegrityError

def menu_estudiante(db):
    
    estudiante_controller = EstudianteController(db)

    while True:
        print("Bienvenido al sistema de gestion de estudiantes")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Obtener estudiante por ID")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            registrar_estudiante(estudiante_controller)
            
        elif opcion == "2":
            listar_estudiantes(estudiante_controller)
            
        elif opcion == "3":
            obtener_estudiante_id(estudiante_controller)
        
        elif opcion == "4":
            actualizar_estudiante(estudiante_controller)
            
        elif opcion == "5":
            eliminar_estudiante(estudiante_controller)
            
        elif opcion == "6":
            print("Saliendo del programa del sistema de estudiantes.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

    
        
def registrar_estudiante(estudiante_controller):
    print("=========== Registrar studiante ==========")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    correo = input("Ingrese el correo electrónico del estudiante: ")
    telefono = input("Ingrese el teléfono del estudiante: ")
    
    try:
        estudiante_controller.registrar_estudiante(nombre, apellido, correo, telefono)
        print("Estudiante registrado con éxito.")
    except IntegrityError:
        print("El correo electrónico ya está registrado.")
    except Exception as e:
        print(f"Error al registrar el estudiante: {e}")
    
def listar_estudiantes(estudiante_controller):
    print("=========== Listar Estudiantes ==========")
    
    try:
       estudiantes = estudiante_controller.listar_estudiantes()
       if estudiantes: 
           print("ID\tNombre\tApellido\tCorreo\tTelefono")
           for estudiante in estudiantes:
               print(f"{estudiante.id_estudiante}\t{estudiante.nombre}\t{estudiante.apellido}\t{estudiante.correo}\t{estudiante.telefono}")
       else:
           print("No hay estudiantes registrados.")
    except Exception as e:
        print(f"Error al listar los estudiantes: {e}")

def obtener_estudiante_id(estudiante_controller):
    print("=========== Obtener Estudiante por ID ==========")
    id_estudiante = input("Ingrese el ID del estudiante: ")
    try:
        estudiante = estudiante_controller.obtener_estudiante_id(id_estudiante)
        if estudiante:
            print(f"ID: {estudiante.id_estudiante}")
            print(f"Nombre: {estudiante.nombre}")
            print(f"Apellido: {estudiante.apellido}")
            print(f"Correo: {estudiante.correo}")
            print(f"Telefono: {estudiante.telefono}")
    except Exception as e:
        print(f"Error al obtener el estudiante: {e}")

def actualizar_estudiante(estudiante_controller):
    print("=========== Actualizar Estudiante ==========")
    id_estudiante = input("Ingrese el ID del estudiante a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del estudiante: ")
    apellido = input("Ingrese el nuevo apellido del estudiante: ")
    correo = input("Ingrese el nuevo correo del estudiante: ")
    telefono = input("Ingrese el nuevo telefono del estudiante: ")

    try:
        estudiante_controller.actualizar_estudiante(id_estudiante, nombre, apellido, correo, telefono)
        print("Estudiante actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el estudiante: {e}")

def eliminar_estudiante(estudiante_controller):
    print("=========== Eliminar Estudiante ==========")
    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")
    try:
        estudiante_controller.eliminar_estudiante(id_estudiante)
        print("Estudiante eliminado correctamente.")

    except Exception as e:
        print(f"Error al eliminar el estudiante: {e}")

        
        
 