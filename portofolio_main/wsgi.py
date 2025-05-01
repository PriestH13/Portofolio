import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

# Configura logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Aggiungi il percorso del progetto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imposta il modulo delle impostazioni
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

try:
    application = get_wsgi_application()
    logger.info("WSGI application started successfully.")
except Exception as e:
    logger.error(f"Error starting WSGI application: {str(e)}")
    raise
