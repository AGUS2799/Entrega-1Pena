# Instrucciones para ejecutar este proyecto

- Clonar el proyecto
```bash
git clone https://github.com/coder-live-class/django-coderhouse-project.git

cd django-coderhouse-project

- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_coder

python manage.py migrate
```

- Ejecutar proyecto
```bash
python manage.py runserver

- Entrar a 
```bash
http://127.0.0.1:8000/app-1/
