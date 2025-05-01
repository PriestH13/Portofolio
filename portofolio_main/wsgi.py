# wsgi.py
import os
import sys
from django.core.wsgi import get_wsgi_application

# Aggiungi il percorso assoluto della directory radice del progetto
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

# Imposta il modulo delle impostazioni
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

application = get_wsgi_application()