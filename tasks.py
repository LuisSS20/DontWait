from invoke import task, run
"""
Archivo de tareas para el proyecto

Para ejecutar una tarea usar: invoke <tarea>
"""


@task
def check_good_pratices(c):
    """
    Comprueba buenas prácticas de los ficheros .py
    """

    print("Compruebo buenas prácticas")
    c.run("pylint src")


@task
def check_sintax(c):
    """
    Comprueba si la sintaxis de los ficheros .py son correctos
    """

    print("Compruebo sintaxis")
    c.run("python3.9 -m compileall src")


@task
def tests(c):
    """
    Realización comprobación de tests
    """

    print("Ejecuto tests")
    c.run("pytest")
