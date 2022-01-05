# Contenedor Docker

## Requisitos
Se necesitara un contenedor que pueda ejecutar código de python, que sea de tamaño reducido, que no tarde mucho en construirse y que ejecute rápidamente los tests.

## Búsqueda de imagen
Primero intenté usar imágenes de una distribución oficial, ubuntu 18.04 y debian. Al usar esta opción tenemos que instalar python3.9 en el dockerfile. Sin embargo el tamaño de estos contenedores eran muy pesados, asi que decidí buscar entre las imagenes oficiales del lenguaje Python.

Partiendo de las imágenes oficiales de python que nos ofrece docker hub, escogí las tres siguientes, ya que informandome por internet, ví que ambas se ajustaban al criterio de tamaño reducido:
1. 3.9-slim-buster: Esta imagen contiene los paquetes mínimos necesarios para ejecutar python, por lo tanto es ideal.
2. 3.9-slim-bullseye: Usa una versión más actualizada de Debian LTS.
3. 3.9-alpine: Es la imagen más recomendada para no tener problemas de espacio, sin embargo puede causar problemas de compatibilidad (en mi caso me dió un error al intentar instalar poetry con una dependencia de una librería, lo arreglé usando RUN apk add gcc libc-dev libffi-dev bash y no descarté esta imagen al poder arreglar el problema).

Una vez los contenedores ya creados comparé el tamaño que tenían.

## Comparando tamaños
3.9-slim-buster ->      REPOSITORY      TAG          IMAGE ID       CREATED             SIZE
                        p_slim-buster   Dockerfile   5f57d3de903f   34 minutes ago      175MB

3.9-slim-bullseye ->    REPOSITORY   TAG          IMAGE ID       CREATED              SIZE
                        p_bullseye   latest       1a8788af2995   About a minute ago   183MB

3.9-alpine      ->      REPOSITORY   TAG          IMAGE ID       CREATED          SIZE
                        p_alpine     latest       c9043af24f3d   16 seconds ago   238MB

Sabiendo que slim-buster usa una versión más antigua que slim-bullseye y que prácticamente el tamaño que ocupan ambas son iguales, decidí descartar slim-buster.

## Comparando velocidad al hacer build
Al hacer el build del contenedor usando slim-bullseye tardaba una media de entre 23 y 26 segundos:
**docker build -t "p_bullseye" .  0,05s user 0,06s system 0% cpu 25,944 total**

Al hacer el build del contenedor usando alpine tardaba una media de entre 45 y 50 segundos:
**docker build -t "p_alpine" .  0,04s user 0,08s system 0% cpu 48,825 total**

## Comparando velocidad tests
Al ejecutar varias veces los test usando el contenedor de slim-bullseye, el tiempo que tardaba eran entre 0.03 segundos y 0.04 segundos.

Al ejecutar un par de veces los test usando el contenedor de alpine, el tiempo que tardaba en todas las ejecuciones era de 0.03 segundos.

Hay que tener en cuenta que los tiempos obtenidos están aproximados por lo que pueden variar en las centésimas.

## Elección
En resumente, tenemos que:
1. Respecto al tamaño de los contenedores, slim-bullseye es un poco menos pesado que usando alpine (una diferencia de 60mb).
2. Respecto al tiempo de construcción de los contenedores, slim-bullseye es el doble de rápido que alpine.
3. Respecto al tiempo de ejecución de tests, ambos son igual de rápidos.

Por lo tanto, la imagen que se ha usado es **slim-bullseye.**


# Justificación uso de poetry config virtualenvs.create false
Para que el build funcione correctamente se debe usar esta opción para que poetry NO instale las dependencias en su entorno virtual, ya que no necesitamos nuevos entornos virtuales en este contenedor que ejecuta una sola aplicación.