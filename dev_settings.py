INSTALLED_APPS = [
    # These are needed for django-admin to run
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # Our precious app
    'account',
]

# A temporary database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

# A dummy secret key for testing
SECRET_KEY = 'django_account'

# This is required since we replace built-in User model
AUTH_USER_MODEL = 'account.Account'
