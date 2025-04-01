from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']  # 실제 배포할 도메인 입력

INSTALLED_APPS += [
    'storages',  # 배포 환경에서 S3 사용 가능
]