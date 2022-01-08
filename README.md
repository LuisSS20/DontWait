# DontWait

## Descripción problema
En un supermercado surge el problema de las colas en espacios como la pescadería
charcutería, etc... El problema principal es predecir el intervalo de tiempo
entre cliente y cliente para que estos puedan seguir comprando en otras zonas,
sin tener que perder tiempo en la cola.

## Instalación
Necesitamos instalar el gestor de dependencias elegido, en mi caso [Poetry](docs/objetivo-3.md).
Seguimos los pasos de la [documentación oficial](https://python-poetry.org/docs/#installation) para poder instalarlo:
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Instalación del resto de dependencias
Ahora para instalar las dependencias, los siguientes pasos son: clonar el repositorio, hacemos `cd` para entrar
y por último `poetry install`.

Al hacer esto, también estamos instalando Invoke, ya que lo hemos incluido en el archivo pyproject.toml.


### Uso

Podemos ver la lista de tareas definidas con:
```shell
invoke --list
```

Para poder comprobar la sintaxis usamos:
```shell
 invoke check
```

Para poder comprobar los tests usamos:
```shell
invoke test
```

Para poder comprobar los tests ejecutando el contenedor docker:
```shell
invoke docker-test
```

## Principios F.I.R.S.T
En los tests desarrollados, he seguido los pasos F.I.R.S.T.
- **Fast** -> Porque los test son rapidos, he tenido que modificar un test que usaba sleep para pasar este requisito.
- **Independent** -> No dependen los unos de los otros.
- **Repeatable** -> El resultado de los test son los mismos independientemente de donde se ejecuten.
- **Self-validating** -> Se podrian ejecutar de manera automatica. 

## Documentación adicional

### Historias de usuarios.

Si quiere informarse acerca de las historias de usuario, hágalo [aquí](docs/usuarios.md).

### Elección de gestor de tareas y dependencias.
Si quiere informarse acerca de las elecciones de gestor de tareas y depencias, hágalo [aquí](docs/objetivo-3.md).

### Elección de herramienta para tests.
Si quiere informarse acerca de las elecciones de la herramienta de tests, hágalo [aquí](docs/objetivo-4.md).

### Documentación relativa al objetivo 5.
Si quiere informarse acerca de la documentación del objetivo 5, hágalo [aquí](docs/objetivo-5.md).
