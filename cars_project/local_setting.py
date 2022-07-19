# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a+zr7403wid2%icq9835iq^@$w8k)q%gux2*m(swmhn3ootojh'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'USER': 'root',
        'PASSWORD': '242234tt34',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

