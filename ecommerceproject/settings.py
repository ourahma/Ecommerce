from pathlib import Path
import os
from dotenv import load_dotenv


# Load the .env file
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-el+j7d_xa82w_ozam%qv&z5876mutygf8lrs&y4io6%*h=1tzw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'paypal.standard.ipn',
    'cart',
    'ecommerceapp.apps.EcommerceappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerceproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerceproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login_user/'
LOGOUT_URL = '/logout/'

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

mail=os.environ.get("MAIL")
<<<<<<< HEAD
DEFAULT_FROM_EMAIL =os.environ.get("mail")
mail_pass=os.environ.get("MAIL_PASSWORD")
print(mail)
=======
mail_pass=os.environ.get("MAIL_PASSWORD")

>>>>>>> 9a7a0e255a2457621c4ad9a03d5356a66f9b2a78
## Mailing backend

EMAIL_LOG_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = mail
EMAIL_HOST_PASSWORD = mail_pass
DEFAULT_FROM_EMAIL = mail
EMAIL_SUBJECT_PREFIX = "Réinitialisation de mot de passe"

#payement 
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL =os.environ.get("PAYPAL_RECEIVER_EMAIL")
PAYPAL_CLIENT_ID=os.environ.get("CLIENT_ID")
PAYPAL_SECRET=os.environ.get("SECRET_KEY")
<<<<<<< HEAD

## pay with card

BRAINTREE_MERCHANT_ID = os.environ.get('Merchant_ID')
BRAINTREE_PUBLIC_KEY  = os.environ.get("Public_key")
BRAINTREE_PRIVATE_KEY  = os.environ.get("Private_key")
=======
>>>>>>> 9a7a0e255a2457621c4ad9a03d5356a66f9b2a78
