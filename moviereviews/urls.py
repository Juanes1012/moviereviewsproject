from django.contrib import admin
from django.urls import path, include
from movie import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('statistics/', views.statistics_view, name='statistics'),

    path('signup/', views.signup, name='signup'),

    # Ruta para la app news
    path('news/', include('news.urls')),
]

# Para servir imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    