# Rename the module into local_settings.py and substitute the name
# and user, password, host, port. Good luck!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ezj+e4m@auyzke$5)rnc%r!3%enk5%!lmwb22^md2_okgnqem0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
