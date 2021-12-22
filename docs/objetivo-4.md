### Criterios para elegir herramienta de tests
El criterio principal para elegir la herramienta de test es el tiempo de ejecución,
es decir, eficiencia. También busco que sea lo más sencillo posible a la hora de crear
y que tenga que tenga una amplia comunidad para poder apoyarme en ella a la hora de
buscar información.

Después de investigar por la red que herramientas eran las más populares para poder
cumplir el criterio de amplia comunidad, encontré: ** unittest, pytest y Robot**

Descarté Robot por el criterio de tiempo de ejecución, eficiencia.
Ya que al investigar, encontré en el siguiente [artículo](https://www.fleekitsolutions.com/pytest-vs-robot-automation-testing/) una mención que dice lo siguiente: "With Pytest, Execution time for test cases is reduced to 30-40 percent as compared to the Robot Framework."

Y para dedicirme entre Unittest u PyTest, me basé en el criterio de sintaxis sencilla.
El primero de ellos a la hora de crear un test necesitaba: importar los modulos,
crear una clase y definir las funciones de test dentro de esa clase.

Con Pytest solo tengo que definir las funciones de test y dentro las aserciones.

Por tanto, pytest se acercaba más a cumplir el criterio. Además de permitirme usar
fixtures y darme la posibilidad de ejecutar los tests de manera paralela usando
pytest-xdist.

### Criterio para aserciones
Como criterio a la hora de elegir una libreria de aserciones ha sido la simplicidad
de la sintaxis. 

Como opciones tenía assertpy y grappa. Si bien podría usar unittest para utilizar sus aserciones, yo no lo considero su uso adecuado, ya que está concebido para realizar test.
Grappa la acabé descartando ya que me informé en internet y la sintaxis era más sencilla con assertpy.


## Test framework: PyTest.

## Biblioteca de aserciones: Assertpy.
