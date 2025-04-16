import os
import sys
from django.core.wsgi import get_wsgi_application

# Obtener la ruta del directorio padre del directorio actual (donde está wsgi.py)
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Añadir el directorio padre al path de Python
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.config.settings')

application = get_wsgi_application()
