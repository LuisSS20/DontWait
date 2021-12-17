from invoke import task, run
"""
Archivo de tareas para el proyecto

Para ejecutar una tarea usar: invoke <tarea>
"""


@task
def check_best_practices(c):
    """
    Comprueba buenas prácticas de los ficheros .py
    """

    print("Compruebo buenas prácticas")
    c.run("pylint src")


@task
def check(c):
    """
    Comprueba si la sintaxis de los ficheros .py son correctos
    """

    print("Compruebo sintaxis")
    c.run("python3.9 -m compileall src")


@task
def test(c):
    """
    Comprobación de tests
    """

    print("Ejecuto tests")
    c.run("pytest")
