from invoke import task, run
"""
Archivo de tareas para el proyecto

Para ejecutar una tarea usar: invoke <tarea>
"""


@task
def check(c):
    """
    Comprueba si la sintaxis de los ficheros .py son correctos
    """

    print("Compruebo sintaxis")
    c.run("pylint src")
