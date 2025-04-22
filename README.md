
# 🚀 Render-Deply-Tutorial-Django-Code

Curso Python con Django, ejercicios para desplegar una aplicación Django utilizando buenas prácticas de estructura, organización y despliegue en **Render**.

![Django Logo](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)
![Render](https://img.shields.io/badge/Deployed%20on-Render-blue?logo=render&logoColor=white)
![GitHub](https://img.shields.io/badge/Version-Control-Git-black?logo=git)

---

## 📜 Descripción General

Este proyecto configura una aplicación Django con múltiples apps, archivos estáticos, plantillas HTML, y soporte para despliegue con Render.

---

## 🛠️ Tecnologías Utilizadas

- 🐍 Python 3.x
- 🌐 Django 4.x
- 🗃️ SQLite
- 🧾 HTML/CSS
- ☁️ Render.com
- 🧪 Git / GitHub

---

## 📁 Estructura del Proyecto

```
Render-Deply-Tutorial-Django-Code/
├── config/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── templates/
│   │       └── index.html
│   ├── manage.py
│   ├── db.sqlite3
│   └── staticfiles/
├── gestion_usu/
│   └── templates/
│       └── gestion_usu/
├── gestion_usuarios/
│   └── templates/
│       └── gestion_usuarios/
├── mycalendar/
├── requirements.txt
├── render.yaml
├── Procfile
├── .gitignore
└── README.md
```

---

## 🧪 Cómo ejecutar el proyecto localmente

```bash
git clone https://github.com/GenX77/Python_Django20042025.git
cd Render-Deply-Tutorial-Django-Code/

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 👤 Autor

Desarrollado por **[GenX]**  
🔗 Repositorio: [https://github.com/GenX77/Python_Django20042025.git](https://github.com/GenX77/Python_Django20042025.git)
