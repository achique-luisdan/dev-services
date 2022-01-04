# Dev Services

Sitio Web de Servicios de Desarrollo


## Instalación (install)

Sigue estos pasos para lograr tener en funcionamiento nuestro proyecto del Backend con Python - Django - Django Rest Framework.

### Paso 0. Clonar repositorio

Teniendo instalado el Git en tu ordenador y despues de autenticarte con GitHub en tu consola:
Recuerda que reciente GitHub como medida de seguridad creo algo llamado: Personal access tokens
Para iniciar sesión de forma seguran en las consolas.

```
git clone https://github.com/achique-luisdan/dev-services.git
```

### Paso 1. Crear entorno virtual

```
virtualenv dev-services
```

### Paso 2. Activar entorno virtual

```
dev-services\Scripts\activate
```

### Paso 3. Instalar paquetes necesario mediante PIP

```
pip install -r dev.txt
```

### Paso 4. Encender servidor local de Django

```
python manage.py runserver
```
