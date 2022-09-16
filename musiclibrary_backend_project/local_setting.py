
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ihha)h*y=(s1mc@o4i$^+9v2ir$5t$k-qy=^6@wba3)a^lv&s5'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}