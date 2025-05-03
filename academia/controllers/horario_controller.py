from models.horario import Horario

class HorarioController:
    def __init__(self, db):
        self.db = db

    def registrar_horario(self, id_curso, dia, hora_inicio, hora_fin):
        """
        Registra un nuevo horario en la base de datos.

        Args:
            id_curso (int): El ID del curso al que se le asigna el horario.
            dia (str): El dia de la semana en el que se imparte el curso.
            hora_inicio (str): La hora de inicio del curso.
            hora_fin (str): La hora de fin del curso.
        """
        sql = """
            INSERT INTO horarios (curso_id, dia_semana, hora_inicio, hora_fin)
            VALUES (%s, %s, %s, %s)
        """
        params = (id_curso, dia, hora_inicio, hora_fin)
        self.db.execute_query(sql, params)

    def listar_horarios(self):
        """
        Lista todos los horarios disponibles en la base de datos.

        Args:
            id_curso (int): El ID del curso al que se le asigna el horario.
            dia (str): El dia de la semana en el que se imparte el curso.
            hora_inicio (str): La hora de inicio del curso.
            hora_fin (str): La hora de fin del curso.
        """
        sql = """SELECT h.id_horario, h.dia_semana, h.hora_inicio, h.hora_fin, c.id_curso, c.nombre 
             FROM horarios h 
             JOIN cursos c 
             ON h.curso_id = c.id_curso"""
        
        return [Horario(*resultado) for resultado in self.db.execute_select(sql)]
    
    def obtener_horario_por_id(self, id_horario):
        """
        Obtiene un horario por su ID.

        Args:
            id_horario (int): El ID del horario a obtener.
        """
        sql = """SELECT h.id_horario, h.dia_semana, h.hora_inicio, h.hora_fin, c.id_curso, c.nombre 
        FROM horarios h 
        JOIN cursos c 
        ON h.curso_id = c.id_curso
        WHERE h.id_horario = %s"""
        params = (id_horario,)
        resultado = self.db.execute_select(sql, params)
        return Horario(*resultado[0]) if resultado else None
    
    def actualizar_horario(self, id_horario, dia_semana, hora_inicio, hora_fin, curso_id):
        """
        Actualiza los datos de un horario existente.

        :param id_horario: ID del horario a actualizar
        :param dia_semana: nuevo día de la semana
        :param hora_inicio: nueva hora de inicio
        :param hora_fin: nueva hora de fin
        :param curso_id: nuevo ID del curso
        """
        sql = """UPDATE horarios SET dia_semana = %s, hora_inicio = %s, hora_fin = %s, curso_id = %s WHERE id_horario = %s"""
        params = (dia_semana, hora_inicio, hora_fin, curso_id, id_horario)
        self.db.execute_query(sql, params)

    def eliminar_horario(self, id_horario):
        """
        Elimina un horario por su ID.

        Args:
            id_horario (int): El ID del horario a eliminar.
        """
        sql = """
            DELETE FROM horarios WHERE id_horario = %s
        """
        params = (id_horario,)
        self.db.execute_query(sql, params)
    


