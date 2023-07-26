from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),          # 資料庫名稱
        'USER': os.getenv("DB_USER"),          # 資料庫使用者名稱
        'PASSWORD': os.getenv("DB_PASS"),      # 資料庫密碼
        'HOST': os.getenv("DB_HOST"),          # PostgreSQL 主機地址
        'PORT': os.getenv("DB_PORT"),          # PostgreSQL 主機端口 (預設為 5432)
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{os.getenv("RD_HOST")}:{os.getenv("RD_PORT")}/1',  
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
