import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key")

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"


# Render exige que você adicione o domínio EXATO:
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "bookstore-new-635l.onrender.com",   
]

# Render define a variável 'RENDER_EXTERNAL_HOSTNAME'
if os.environ.get('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(os.environ.get('RENDER_EXTERNAL_HOSTNAME'))

# -------------------------------------------------------------------
# APLICAÇÕES
# -------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps do projeto
    "bookstore",
    "product",
    "order",

    # Django REST Framework
    "rest_framework",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer"
    ]
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore.wsgi.application"

# -------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# -------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# STATIC FILES — obrigatório no Render
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Caso você use arquivos de mídia:
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------------------------------------------
# DJANGO SECURITY PARA PRODUÇÃO
# -------------------------------------------------------------------
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        "https://bookstore-new-635l.onrender.com",
    ]
else:
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost",
        "http://127.0.0.1",
    ]



    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# -------------------------------------------------------------------
# DEFAULT
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



