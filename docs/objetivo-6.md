# Integración continua

## Tareas a realizar
1. Ejecución automática de los tests desarrollados cada vez que se solicite un pull request.
2. Comprobación de la ejecución correcta del código usando diferentes versiones del lenguaje usado.

Estas tareas se enmarcan dentro de lo catalogado como Integración Continua (CI), que consiste en comprobar que cada cambio nuevo realizado en nuestro repositorio ha sido válidado y aceptado.

### Requisitos
Para poder realizar las tareas, hace falta seleccionar un sistema de CI, para ello se han seleccionado unos requisitos para poder elegirlo:

1. Compatible con GitHub, ya que es nuestro sistema de control de versiones.
2. Que sea un servicio gratuito y que no dependa de periodos de prueba.
3. Que no tengan que realizarse instalaciones.

## Sistemas de CI evaluados
### [Jenkins](https://www.jenkins.io/)
Jenkins es un servidor de automatización open source escrito enteramente en Java. Con jenkins se puede realizar pruebas de automatización usando frameworks como PyTest, Robot..., compilar software usando Gradle y Maven, usarlo para CI...
**[x] Compatible con GitHub.** Jenkins soporta la integración tanto con GitHub como GitHub Enterprise
**[x] Servicio gratuito.** Es gratis al ser open source, sin embargo se necesita de un servidor para hostearlo y este servidor requerirá de un mantenimiento.
**[] No instalaciones.** Por desgracia, para usar Jenkins hace falta realizar una instalación, por tanto no cubre este requisito.

**Jenkins queda descartado como sistema de CI por no cumplir todos los requisitos**

### [CircleCI](https://circleci.com/)
CircleCI es uno de los sistemas de integración más usados y más versátiles que hay. Su configuración se realiza através de un fichero .yml y es bastante sencillo hacerlo.  
**[x] Compatible con GitHub.** Si, tiene soporte con GitHub.
**[x] Servicio gratuito.** Es totalmente gratuito, aunque esta limitado a 6000 minutos de build al mes. También hay varios planes de pago.
**[x] No instalaciones.** Está basado en nube, por tanto no necesitaríamos una instalación para poder usarlo.

**CircleCI es una opción viable para usar como un sistema de CI**

### [GitHub Actions](https://github.com/features/actions)
GitHub nos ofrece una manera bastante sencilla de poder incorporar CI a nuestros repositorios. Con este sistema podemos determinar que se lancen nuestros tests, desplegar nuestra aplicación e incluso herramientas de revisión de código.
**[x] Compatible con GitHub.** Sí, como puede ser obvio.
**[x] Servicio gratuito.** Sí, es gratuito con cierta limitaciones. 
**[x] No instalaciones.** Se realiza todo en la nube, así que no es necesaria realizar alguna instalación.

**GitHub Actions es una opción viable para usar como un sistema de CI**

### [GitLab CI](https://docs.gitlab.com/ee/ci/)
GitLab CI es una alternativa acertada para la integración continua en nuestros repositorios. Cuenta con una configuración bastante similar a CircleCI.
**[x] Compatible con GitHub.** Sí, es compatible con GitHub y se configura através de un fichero .yml.
**[x] Servicio gratuito.** Sí, tiene un servicio gratuito limitado a 400 minutos/mes de CI/CD. También ofrecen varios planes nos dan más prestaciones a cambio de una mensualidad.
**[x] No instalaciones.** Basado en la nube como otros sistemas CI, no require de instalación en el host.

**GitLab CI es una opción viable para usar como un sistema de CI**

### [Bamboo](https://www.atlassian.com/es/software/bamboo)
Bamboo es una herramienta comercial para la integración continua. Aunque se puede solicitar gratuitamente su software através de [esta solicitud](https://www.atlassian.com/software/views/open-source-license-request).  
**[x] Compatible con GitHub.** Sí, bamboo nos brinda esa posibilidad.
**[x] Servicio gratuito.** Si se solicita la licencia gratuita para proyectos de código abierto es gratuito. A su vez nos ofrece un trial de 30 días para pRobar la herramienta.
**[] No instalaciones.** El servicio que ofrece Bamboo no es en la nube, se necesita tener instalado java e instalar Bamboo.

**Bamboo queda descartado como sistema de CI, ya que no cumple el requisito de no instalaciones y, además, aunque parcialmente cubre el de servicio gratuito, esperar a la concesión de una licencia gratuito es inviable.**

## Elección final
De los sistemas de CI evaluados, nos quedamos con CircleCI, GitLab CI y GitHub Actions, ya que cumplen con los requisitos.
A elección personal, he considerado usar **GitHub Actions** para poder comprobar la ejecución correcta del código usando diferentes versiones del lenguaje Pyhon, ya que es bastante sencillo de configurar y lo he usado anteriormente, por lo que estoy familiarizado con él.
Entre CircleCI y GitLab CI, me quedo con **GitLab CI** ya que, aunque ambos son similares a la hora de configurarlos, me resulta más simple la sintaxis para la creación del fichero de configuración .yml. Al elegir **GitLab CI** me dí cuenta que es necesario introducir una tarjeta para poder verificar el usuario en GitLab CI, en mi caso, me informé y esto es para que los usuarios no abusen y creen multicuentas. En mi caso, introducí una tarjeta virtual para evitar cargos no autorizados y pude comprobar como te devuelven (un rato más tarde) el importe que para realizar esta verificación (1$).

## Justificación versiones de python a testear

El principal criterio usado para tener una versión de partida es el tiempo restante de soporte que les quedan a las diferentes versiones de Python.
Sabiendo esto, tenemos que la última versión la cual ya no tiene soporte es Python 3.6([consulta aquí](endoflife.date/python)). Ahora tenemos las siguientes versiones disponibles para testear que cumple con el criterio de soporte: **3.7, 3.8, 3.9 y 3.10.**

La versión **3.9** no se testeará usando GitHub Actions, debido a que ya se testea en el docker usado con el check de GitLab.
Considero oportuno añadir la version **3.10** ya que, aunque es bastante reciente(release 04/10/2021) y no es usada tanto como otras versiones anteriores, creo que es buena práctica añadir las versiones más recientes.

En conclusión, con GitHub Actions se ejecutaran los test usando las versiones **3.7, 3.8, 3.9 y 3.10.**