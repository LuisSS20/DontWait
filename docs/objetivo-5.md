# Contenedor Docker

## Requisitos
Se necesitara un contenedor que pueda ejecutar código de python y que sea de tamaño reducido, ya que su funcionalidad es la ejecución de los tests desarrollados anteriormente.

## Búsqueda de imagen
Primero intenté usar imágenes de una distribución oficial, ubuntu 18.04 y debian. Al usar esta opción tenemos que instalar python3.9 en el dockerfile. Sin embargo el tamaño de estos contenedores eran muy pesados, asi que decidí buscar entre las imagenes oficiales del lenguaje Python.

Partiendo de las siguientes imágenes oficiales de python que nos ofrece docker hub, escogí las dos siguientes, ya que informandome por internet, ví que ambas se ajustaban al criterio de tamaño reducido:
1. 3.9-slim-buster: Esta imagen contiene los paquetes mínimos necesarios para ejecutar python, por lo tanto es ideal.
3. 3.9-alpine: Es la imagen más recomendada para no tener problemas de espacio, sin embargo puede causar problemas de compatibilidad (en mi caso me dió un problema al intentar instalar poetry, lo arreglé y no descarté esta imagen).

Una vez los contenedores ya creados comparé el tamaño que tenían para saber cuál escoger.

3.9-slim-buster -> REPOSITORY      TAG          IMAGE ID       CREATED             SIZE
                   p_slim-buster   Dockerfile   5f57d3de903f   34 minutes ago      175MB

3.9-alpine      -> REPOSITORY   TAG          IMAGE ID       CREATED          SIZE
                   p_alpine     Dockerfile   1a8304643ec4   15 minutes ago   350MB

## Elección
Al comprobar que la imagen de alpine ocupaba el doble, la descarté y opté por usar slim-buster.


# Justificación uso de poetry config virtualenvs.create false
Para que el build funcione correctamente se debe usar esta opción para que poetry NO instale las dependencias en su entorno virtual.