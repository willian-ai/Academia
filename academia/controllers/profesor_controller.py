from models.profesor import Profesor

class ProfesorController:
    def __init__(self, db):
        self.db = db
        
    def registrar_profesor(self, nombre, apellido, correo, telefono, especialidad):
        """
        Registra un nuevo profesor en la base de datos.
        
        Args:
            nombre (str): El nombre del profesor.
            apellido (str): El apellido del profesor.
            correo (str): El correo electrónico del profesor.
            telefono (str): El número de teléfono del profesor.
            especialidad (str): La especialidad del profesor.
        """
        sql = """
            INSERT INTO profesores (nombre, apellido, correo_electronico, telefono, especialidad)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(sql, (nombre, apellido, correo, telefono, especialidad))

    def listar_profesores(self):
        """
        Devuelve una lista de todos los profesores registrados en la base de datos.

        Args:
            nombre (str): El nombre del profesor.
            apellido (str): El apellido del profesor.
            correo (str): El correo electrónico del profesor.
            telefono (str): El número de teléfono del profesor.
            especialidad (str): La especialidad del profesor.
        """
        sql = """
            SELECT id_profesor, nombre, apellido, correo_electronico, telefono, especialidad
            FROM profesores
        """
        resultados = self.db.execute_select(sql)
        return [Profesor(*resultado) for resultado in resultados]

    def obtener_profesor_id(self, id_profesor): 
        """
        Obtiene un profesor específico por su ID.

        Args:
            id_profesor (int): El ID del profesor a obtener.
        """
        sql = """
            SELECT id_profesor, nombre, apellido, correo_electronico, telefono, especialidad
            FROM profesores
            WHERE id_profesor = %s
        """
        params = (id_profesor,)
        resultados = self.db.execute_select(sql, params)
        return Profesor(*resultados[0]) if resultados else None 
    
    def actualizar_profesor(self, id_profesor, nombre, apellido, correo, telefono, especialidad):
        """
        Actualiza los datos de un profesor existente.

        Args:
            id_profesor (int): El ID del profesor a actualizar.
            nombre (str): El nuevo nombre del profesor.
            apellido (str): El nuevo apellido del profesor.
            correo (str): El nuevo correo electrónico del profesor.
            telefono (str): El nuevo número de teléfono del profesor.
            especialidad (str): La nueva especialidad del profesor.
        """
        sql = """
            UPDATE profesores
            SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s, especialidad = %s
            WHERE id_profesor = %s
        """
        params = (nombre, apellido, correo, telefono, especialidad, id_profesor)
        self.db.execute_query(sql, params)

    def eliminar_profesor(self, id_profesor):
        """
        Elimina un profesor específico por su ID.

        Args:
            id_profesor (int): El ID del profesor a eliminar.
        """
        sql = """
            DELETE FROM profesores WHERE id_profesor = %s
        """
        params = (id_profesor,)
        self.db.execute_query(sql, params)
        

