### Criterios para elegir herramienta de tests
El criterio principal para elegir la herramienta de test es el tiempo de ejecución,
es decir, eficiencia. También busco que sea lo más sencillo posible a la hora de crear
y que tenga que tenga una amplia comunidad para poder apoyarme en ella a la hora de
buscar información.

Después de investigar por la red que herramientas eran las más populares para poder
cumplir el criterio de amplia comunidad, encontré: **pytest y Robot**

Descarté Robot por el criterio de tiempo de ejecución, eficiencia, ya que al investigar,
encontré en el siguiente [artículo](https://www.fleekitsolutions.com/pytest-vs-robot-automation-testing/)
una mención que dice lo siguiente: "With Pytest, Execution time for test cases is reduced to 30-40 percent as compared to the Robot Framework."

A su vez la sintaxis de Pytest me resultaba mñas sencilla que Robot.

Algo que me gustó de Pytest es que permitirme usar fixtures y da la posibilidad de ejecutar
los tests de manera paralela usando pytest-xdist.

### Criterio para aserciones
Como criterio a la hora de elegir una libreria de aserciones ha sido la simplicidad
de la sintaxis. 

Como opciones principales tenía assertpy y grappa. Aunque existen otras como unittest, verify...
Grappa la acabé descartando ya que me informé en internet y la sintaxis era más sencilla con assertpy.


## Test framework: PyTest.

## Biblioteca de aserciones: Assertpy.
