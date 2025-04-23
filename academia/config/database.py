import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector.errors import IntegrityError
from mysql.connector import Error
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class  Database:
    
    def __init__(self):
        self.conection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wil83031500%&",
            database = "academia",
            port = 3306,
            charset='utf8mb4',
            collation='utf8mb4_spanish_ci'            
        )
        self.cursor = self.conection.cursor()
    
    def _execute(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
    
        except IntegrityError as e:
            raise  Exception(f"Error de Integracion: {e.msg}")
        except Error as e:
            raise  Exception(f"Error al ejecutar la consulta: {e.msg}")
    
    def execute_query(self, query, params=None):
        self._execute(query, params)
        self.conection.commit()
    
    def execute_select(self, query, params=None):
        self._execute(query, params)
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.cursor.close()
        self.conection.close()
    
    