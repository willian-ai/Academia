from models.estudiante import Estudiante

class EstudianteController:
    def __init__(self, db):
        self.db = db
    
   
        
    def registrar_estudiante(self, nombre, apellido, correo, telefono):
        """
        Registra un nuevo estudiante en la base de datos.
        
        Args:
            nombre (str): El nombre del estudiante.
            apellido (str): El apellido del estudiante.
            correo (str): El correo electrónico del estudiante.
            telefono (str): El número de teléfono del estudiante.
            
        """
        sql = """
        INSERT INTO estudiantes (nombre, apellido, correo_electronico, telefono)
        VALUES ( %s, %s, %s, %s)
        """
        params = (nombre, apellido, correo, telefono)
        self.db.execute_query(sql, params)
        
       
           
    def listar_estudiantes(self):
        """
        Devuelve una lista de todos los estudiantes registrados en la base de datos.

        """
        sql = """
            SELECT id_estudiante, nombre, apellido, correo_electronico, telefono 
            FROM estudiantes"""
        
        resultados = self.db.execute_select(sql)
        return [Estudiante(*resultado) for resultado in resultados]  
        
            
    def obtener_estudiante_id(self, id_estudiante):
        """
        Obtiene un estudiante específico por su ID.
        
        Args:
            id_estudiante (int): El ID del estudiante a obtener.
            
        Returns:
            Estudiante: El objeto Estudiante si se encuentra, None si no existe.
        """
        sql = """
            SELECT id_estudiante, nombre, apellido, correo_electronico, telefono 
            FROM estudiantes 
            WHERE id_estudiante = %s
        """
        params = (id_estudiante,)
        resultados = self.db.execute_select(sql, params)
        
        if not resultados:
            return None
            
        # Asegurarse de que tenemos exactamente un resultado
        if len(resultados) > 1:
            raise ValueError(f"Se encontraron múltiples estudiantes con el ID {id_estudiante}")
            
        # Obtener el primer y único resultado
        estudiante_data = resultados[0]
        
        # Verificar que tenemos todos los campos necesarios
        if len(estudiante_data) != 5:
            raise ValueError("Los datos del estudiante no tienen el formato esperado")
            
        return Estudiante(*estudiante_data)
        
        
    def actualizar_estudiante(self, id_estudiante, nombre, apellido, correo, telefono):
        """
        Actualiza los datos de un estudiante existente.
        
        Args:
        
        :param id_estudiante: El ID del estudiante a actualizar.
        :param nombre: El nuevo nombre del estudiante.
        :param apellido: El nuevo apellido del estudiante.
        :param correo: El nuevo correo electrónico del estudiante.
        :param telefono: El nuevo número de teléfono del estudiante.    
        
        """
        sql = """
            UPDATE estudiantes 
            SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s 
            WHERE id_estudiante = %s
        """
        params = (nombre, apellido, correo, telefono, id_estudiante)
        self.db.execute_query(sql, params)
        
        
    def eliminar_estudiante(self, id_estudiante):
        """
        Elimina un estudiante específico por su ID.
        
        Args:
            id_estudiante (int): El ID del estudiante a eliminar.

        """
        sql = """
            DELETE FROM estudiantes WHERE id_estudiante = %s
        """
        params = (id_estudiante,)
        self.db.execute_query(sql, params)
        
        
        
        
        
