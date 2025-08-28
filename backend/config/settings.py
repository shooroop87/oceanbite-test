import io
import os
import sys
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "1insecure1-1default1")

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost 127.0.0.1").split()

CSRF_TRUSTED_ORIGINS = [
    "https://*.oceanbiteseafood.com",
    "https://oceanbiteseafood.com",
    "http://localhost",
    "http://localhost:8000",
    "http://backend-1:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    # 3rd party
    "easy_thumbnails",
    "filer",
    "mptt",
    "parler",
    "django_ckeditor_5",
    "taggit",
    "meta",
    # local
    "core",
]

if DEBUG:
    INSTALLED_APPS += ["django_browser_reload"]

MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
if DEBUG:
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "core" / "templates",  # Основные шаблоны
            BASE_DIR / "templates",           # Общие шаблоны (если появятся)
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "core.context_processors.default_schema",
                "core.context_processors.tours_context",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "oceanbite_seafood"),
        "USER": os.getenv("POSTGRES_USER", "oceanbite_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": int(os.getenv("DB_PORT", 5432)),
    }
}

DEFAULT_CHARSET = "utf-8"
FILE_CHARSET = "utf-8"

LANGUAGE_CODE = "en"
TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ("en", "English"),
    ("fr", _("French")),
    ("de", _("German")),
    ("es", _("Spanish")),
    ("nl", _("Dutch")),
]

LOCALE_PATHS = [BASE_DIR / "core" / "locale"]

# Static & media
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "core" / "static"]
STATIC_ROOT = BASE_DIR / "collected_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

FILE_UPLOAD_PERMISSIONS = 0o644  # rw-r--r--
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755  # rwxr-xr-x

# Создаем медиа-директорию если не существует
os.makedirs(MEDIA_ROOT, exist_ok=True)

# Filer / thumbnails
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_QUALITY = 90
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "easy_thumbnails.processors.scale_and_crop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# Cache / static storage
if DEBUG:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}
else:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.getenv("REDIS_URL", "redis://redis:6379/1"),
            "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        }
    }

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "your-smtp-server.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@domain.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your-password")
DEFAULT_FROM_EMAIL = "Oceanbite Seafood <noreply@oceanbiteseafood.com>"
CONTACT_EMAIL = "info@oceanbiteseafood.com"

CONTACT_PHONE = "+1 (234) 567-890"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

LOGS_DIR = BASE_DIR / "logs"
os.makedirs(LOGS_DIR, exist_ok=True)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}", "style": "{"},
        "simple": {"format": "{levelname} {asctime} {message}", "style": "{"},
        "detailed": {"format": "🐛 {levelname} [{asctime}] {name} {module}:{lineno} - {message}", "style": "{"},
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "detailed"},
        "file_debug": {"level": "DEBUG", "class": "logging.FileHandler", "filename": LOGS_DIR / "debug.log", "formatter": "detailed"},
        "media_file": {"level": "DEBUG", "class": "logging.FileHandler", "filename": LOGS_DIR / "media.log", "formatter": "detailed"},
        "core_file": {"level": "DEBUG", "class": "logging.FileHandler", "filename": LOGS_DIR / "core.log", "formatter": "detailed"},
    },
    "loggers": {
        "core.views": {"handlers": ["core_file", "console"], "level": "DEBUG", "propagate": False},
        "django.core.files": {"handlers": ["media_file", "console"], "level": "DEBUG", "propagate": False},
        "PIL": {"handlers": ["media_file", "console"], "level": "DEBUG", "propagate": False},
        "ckeditor": {"handlers": ["media_file", "console"], "level": "DEBUG", "propagate": False},
        "django.request": {"handlers": ["file_debug", "console"], "level": "DEBUG", "propagate": False},
        "django": {"handlers": ["file_debug"], "level": "INFO", "propagate": False},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}

PARLER_LANGUAGES = {
    None: (
        {"code": "en"},
        {"code": "fr"},
        {"code": "de"},
        {"code": "es"},
        {"code": "nl"},
    ),
    "default": {"fallbacks": ["en"], "hide_untranslated": False},
}

CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
CKEDITOR_5_UPLOAD_PATH = "content/"
CKEDITOR_5_IMAGE_UPLOAD_ENABLED = True
CKEDITOR_5_FILE_UPLOAD_ENABLED = True
CKEDITOR_5_ALLOW_ALL_FILE_TYPES = False
CKEDITOR_5_UPLOAD_FILE_TYPES = ["jpeg","jpg","png","gif","webp","pdf","doc","docx"]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading","|","bold","italic","underline","strikethrough","|",
            "link","uploadImage","blockQuote","|","bulletedList","numberedList","|",
            "outdent","indent","|","insertTable","|","undo","redo"
        ],
    },
}

TAGGIT_CASE_INSENSITIVE = True
THUMBNAIL_FORMAT = "WEBP"
THUMBNAIL_QUALITY = 85
THUMBNAIL_PRESERVE_FORMAT = False
PAGINATE_BY = 10
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
DATA_UPLOAD_MAX_MEMORY_SIZE = 15 * 1024 * 1024
ALLOWED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
MAX_IMAGE_SIZE = 5 * 1024 * 1024
IMAGE_QUALITY = 85
MAX_IMAGE_WIDTH = 1200
MAX_IMAGE_HEIGHT = 1200

THUMBNAIL_ALIASES = {
    "": {
        "admin_thumb": {"size": (100, 75), "crop": True, "quality": 75},
    },
}