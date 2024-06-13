from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken import views


urlpatterns = [
    path(f'{settings.SECRET_URL_PREFIX}admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('blog.urls')),
]
