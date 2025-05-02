import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Configura il logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Aggiungi il percorso del progetto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imposta la variabile di ambiente per le impostazioni Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

try:
    # Crea l'applicazione WSGI
    application = get_wsgi_application()
    logger.info("WSGI application started successfully.")
except Exception as e:
    logger.error(f"Error starting WSGI application: {str(e)}")
    raise e
