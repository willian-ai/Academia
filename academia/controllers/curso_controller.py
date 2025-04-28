from models.curso import Curso

class CursoController:
    def __init__(self, db):
        self.db = db
        
    def registrar_curso(self, nombre, descripcion, duracion_hrs, id_profesor):
        """
        Registra un nuevo curso en la base de datos.
        
        Args:
            nombre (str): El nombre del curso.
            descripcion (str): La descripcion del curso.
            duracion_hrs (int): La duracion del curso en horas.
            id_profesor (int): El ID del profesor que imparte el curso.
            profesor_nombre (str): El nombre del profesor que imparte el curso.
        """
        sql = """
            INSERT INTO cursos (nombre, descripcion, duracion_horas, profesor_id)
            VALUES (%s, %s, %s, %s)
        """
        params = (nombre, descripcion, duracion_hrs, id_profesor)
        self.db.execute_query(sql, params)
        
    def listar_cursos(self):
        """
        Lista todos los cursos disponibles en la base de datos.
        
        Args:
            None
            
        Returns:
            list: Una lista de objetos Curso.
        """
        sql = """
            SELECT c.id_curso, c.nombre, c.descripcion , c.duracion_horas, d.id_profesor, 
            CONCAT(d.nombre, ' ', d.apellido) AS profesor_nombre FROM cursos c 
            JOIN profesores d ON c.profesor_id = d.id_profesor; 
        """
        resultados = self.db.execute_select(sql)
        return [Curso(*resultado) for resultado in resultados]
    
    def obtener_curso_por_id(self, id_curso):
        """
        Obtiene un curso por su ID.
        
        Args:
            id_curso (int): El ID del curso a obtener.
        """
        sql = """
            SELECT c.id_curso, c.nombre, c.descripcion , c.duracion_horas, d.id_profesor, 
            CONCAT(d.nombre, ' ', d.apellido) AS profesor_nombre FROM Cursos c 
            JOIN Profesores d ON c.profesor_id = d.id_profesor WHERE c.id_curso = %s
        """
        params = (id_curso,)
        resultado = self.db.execute_select(sql, params)
        return Curso(*resultado[0]) if resultado else None
    
    def actualizar_curso(self, id_curso, nombre, descripcion, duracion_hrs, id_profesor):
        """
        Actualiza los datos de un curso existente.
        
        Args:
            id_curso (int): El ID del curso a actualizar.
            nombre (str): El nuevo nombre del curso.
            descripcion (str): La nueva descripcion del curso.
            duracion_hrs (int): La nueva duracion del curso en horas.
            id_profesor (int): El nuevo ID del profesor que imparte el curso.
        """
        sql = """
            UPDATE Cursos SET nombre = %s, descripcion = %s, duracion_horas = %s, profesor_id = %s 
            WHERE id_curso = %s
        """
        params = (nombre, descripcion, duracion_hrs, id_profesor, id_curso)
        self.db.execute_query(sql, params)
        
    def eliminar_curso(self, id_curso):
        """
        Elimina un curso por su ID.
        
        Args:
            id_curso (int): El ID del curso a eliminar.
        """
        sql = """
            DELETE FROM Cursos WHERE id_curso = %s
        """
        params = (id_curso,)    
        self.db.execute_query(sql, params)
