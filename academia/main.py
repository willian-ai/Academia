from views.menuEstudiante import menu_estudiante
from views.menuProfesor import menu_profesor
from views.menuCurso import menu_curso
from views.menuHorario import menu_horario
from views.menuMatricula import menu_matricula
from views.viewTkinter.menuPrincipal import MenuPrincipal
from config.database import Database

if __name__ == "__main__":
    db = Database()
    try:
        #menu_estudiante(db)
        #menu_profesor(db)
        #menu_curso(db)
        #menu_horario(db)
        #menu_matricula(db)
        menu_principal = MenuPrincipal()
        menu_principal.ventana.mainloop()
    finally:
        db.close_connection()
