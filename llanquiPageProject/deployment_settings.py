import os
import dj_database_url
from .settings import * 


# ====== ALLOWED HOSTS ======
# Define los hosts permitidos para la aplicación en producción
ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

# ====== CSRF TRUSTED ORIGINS ======
# Define los orígenes de confianza para CSRF
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

# ====== DEBUG ======
# Desactiva el modo de depuración en producción
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ====== SECRET KEY ======
# Obtiene la clave secreta desde las variables de entorno
SECRET_KEY = os.environ.get('SECRET_KEY')

# ====== MIDDLEWARE ======
# Define el middleware utilizado en la aplicación
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ====== CORS CONFIGURATION ======
# Define los orígenes permitidos para CORS
CORS_ALLOWED_ORIGINS = ['https://' + os.environ.get('RENDER_URL_FRONTEND')]

# ====== DATABASE CONFIGURATION ======
# Configura la base de datos utilizando dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# ====== STORAGE CONFIGURATION ======
# Configura el almacenamiento de archivos estáticos y otros archivos
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# ====== LOGGING CONFIGURATION ======
# Configura el envío de errores a los administradores por correo electrónico
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# ====== EMAIL CONFIGURATION ======
# Configura el envío de correos electrónicos para el debug.
ADMINS = [(os.environ.get("ADMIN"), os.environ.get("EMAIL_USER"))]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER_SMTP')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_APP_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER