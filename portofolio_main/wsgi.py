import os
import sys
from django.core.wsgi import get_wsgi_application

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

print(f"Python path: {sys.path}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portofolio_main.settings')

application = get_wsgi_application()