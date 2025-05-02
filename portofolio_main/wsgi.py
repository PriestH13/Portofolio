# portofolio_main/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Imposta il modulo delle impostazioni di Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

# Ottieni l'applicazione WSGI
application = get_wsgi_application()
