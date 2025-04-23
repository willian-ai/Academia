from models.matricula import Matricula

class MatriculaController:
    def __init__(self, db):
        self.db = db

    def registrar_matricula(self, id_estudiante, id_curso, fecha_matricula):
        """
        Registra una nueva matricula en la base de datos.

        Args:
            id_estudiante (int): El ID del estudiante que se matricula.
            id_curso (int): El ID del curso al que se matricula.
            fecha_matricula (str): La fecha de matricula en formato 'YYYY-MM-DD'.
        """
        sql = """
            INSERT INTO matriculas (estudiante_id, curso_id, fecha_matricula)
            VALUES (%s, %s, %s)
        """
        params = (id_estudiante, id_curso, fecha_matricula)
        self.db.execute_query(sql, params)

    def listar_matriculas(self):
        """
        Lista todas las matriculas disponibles en la base de datos.

        Returns:
            list: Lista de objetos Matricula.
        """
        sql = """
            SELECT * FROM matriculas 
            
        """
        return [Matricula(*resultado) for resultado in self.db.execute_select(sql)]
    
    def obtener_matricula_por_id(self, id_matricula):
        """
        Obtiene una matricula por su ID.

        Args:   
            id_matricula (int): El ID de la matricula a obtener.

        Returns:
            Matricula: Objeto Matricula con los datos de la matricula.
        """
        sql = """
            SELECT * FROM matriculas 
            WHERE id_matricula = %s
        """
        params = (id_matricula,)    
        resultado = self.db.execute_select(sql, params)
        return Matricula(*resultado[0]) if resultado else None
    
    def actualizar_matricula(self, id_matricula, id_estudiante, id_curso, fecha_matricula):
        """
        Actualiza los datos de una matricula existente.

        Args:
            id_matricula (int): El ID de la matricula a actualizar.
            id_estudiante (int): El ID del estudiante a actualizar.
            id_curso (int): El ID del curso a actualizar.
            fecha_matricula (str): La fecha de matricula a actualizar en formato 'YYYY-MM-DD'.
        """
        sql = """
            UPDATE matriculas
            SET estudiante_id = %s, curso_id = %s, fecha_matricula = %s
            WHERE id_matricula = %s
        """
        params = (id_estudiante, id_curso, fecha_matricula, id_matricula)
        self.db.execute_query(sql, params)

    def eliminar_matricula(self, id_matricula):
        """
        Elimina una matricula de la base de datos.

        Args:
            id_matricula (int): El ID de la matricula a eliminar.
        """
        sql = """
            DELETE FROM matriculas
            WHERE id_matricula = %s
        """
        params = (id_matricula,)
        self.db.execute_query(sql, params)  
    
        

