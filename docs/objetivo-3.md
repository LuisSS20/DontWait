## Criterios para elegir gestor de tareas y dependencias
**Mis principales criterios eran: popular entre la comunidad, fácil acceso a documentación y una sintaxis simple en la medida de lo posible.**
En un principio tenía cuatro posibles candidatos para el gestor de tareas: **Makefile, Pypyr, Invoke y Poethepoet**.
Poethepoet lo descarté debido a que tenia una menor popularidad en la comunidad.
Makefile lo descarté porque ya lo había usado antes en otros proyectos y me apetecía usar algo nuevo.
Y entre Pypyr e Invoke, decidí Invoke porque me parecía más cómodo.

Para el gestor de dependencias, mis criterios para elegirlos eran los mismos. Tenía como posibles candidatos a Pipenv o Poetry.
Decidí usar Poetry porque la sintaxis me parecía mejor, sin embargo es algo menos popular que Pipenv. Aun así, Poetry es ampliamente usado en la comunidad.

## Gestor de tareas elegido: Invoke.
Python tiene un tasker runner específico, invoke. Es open-source, tiene una sintaxis cómoda y
contiene gran cantidad de [documentación](https://docs.pyinvoke.org/en/stable/).

## Gestor de dependencias elegido: Poetry.
Al igual que con invoke, Poetry tiene una [documentación](https://python-poetry.org/) amplía y buena. La configuración
del archivo principal es muy sencilla (pyproject.toml).