import os
import sys
from django.core.wsgi import get_wsgi_application

# Aggiungi il percorso esplicito per Render e locale
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, '/opt/render/project/src')  # Percorso radice su Render
sys.path.insert(0, os.path.join('/opt/render/project/src', 'Portofolio'))  # Aggiungi Portofolio esplicitamente

# Stampa il percorso per debugging
print(f"Python path: {sys.path}")

# Debug dei file solo se il percorso esiste (evita errori su Windows)
try:
    print(f"Files in BASE_DIR ({BASE_DIR}): {os.listdir(BASE_DIR)}")
    if os.path.exists('/opt/render/project/src'):
        print(f"Files in /opt/render/project/src: {os.listdir('/opt/render/project/src')}")
except FileNotFoundError:
    print("Impossibile accedere a /opt/render/project/src (solo su Render)")

# Imposta il modulo delle impostazioni
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

application = get_wsgi_application()