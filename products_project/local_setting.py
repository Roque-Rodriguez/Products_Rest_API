# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xe#w4d-3wkto+6ne+2xrw*i+z*dx!xf)k904nnlmj_qhq3hcly'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password123',
    }
}


