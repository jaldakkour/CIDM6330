import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for your Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Get the WSGI application
application = get_wsgi_application()
