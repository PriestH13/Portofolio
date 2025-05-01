import os
import sys
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, '/opt/render/project/src')  # Solo questo è necessario su Render

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

application = get_wsgi_application()