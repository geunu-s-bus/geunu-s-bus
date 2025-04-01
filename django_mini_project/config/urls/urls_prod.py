from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),    # 여기에 배포용 URL 패턴 추가
]