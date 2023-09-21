from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'apps.user',
    'apps.resources',
    'apps.core',
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = [*DEFAULT_APPS, *CUSTOM_APPS, *THIRD_PARTY_APPS]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.log.simple_logging_middleware',
    # 'apps.core.middleware.logging.simple_logging_middleware',
    # 'apps.core.middleware.logging.ViewExecutionTimeMiddleware',
    # 'apps.core.middleware.logging.ViewExecutionTime2Middleware',
    # 'apps.resources.middleware.printing.printing_middleware',
    
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR / "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.User"


# storage media 
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"

LOGIN_URL = "login-view" # best practice to use `login-view`

# Logger configuration
LOGGING = {
    'version': 1, # dictConfig format version
    'loggers': { # Receiver or entry point to the logging 
        'logging_mw': { # specify the logger instance
            # decide which handler to handle it
            'handlers': ['file', 'console'], # the 'file' handler will handle
            'level': 'DEBUG', # this will accept all log levels
        }
    },
    
    'handlers': {
        'console': {
            'level': 'DEBUG', # handle this logging level and any other above it
            # TODO: Search for more class options
            'class':  'logging.StreamHandler',  # this defines the medium to send the log messages
            'filters': ['only_if_debug_true'], # Handle only if DEBUG=True
        },
        'file': {
            'level': 'INFO', # handle this logging level and any other above it
            'class':  'logging.FileHandler',  # this defines the medium to send the log messages
            'filename': str(BASE_DIR / 'logs' / "req_res_logs.txt"),
            'formatter': 'verbose',
        },
        
    },
    
    'formatters': {
        'verbose': { # name of formatter
            # TODO: search for more format log variables from the official docs
            'format': '{levelname} {asctime} {module} :: {message}',
            'style': '{', # I want to use curly braces to access attributes 
        }
    },
    'filters': {
        'only_if_debug_true': {
            "()": 'django.utils.log.RequireDebugTrue',
        },
        #TODO: Call your own custom function to handle the filtering
    },
}