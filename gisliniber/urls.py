
from django.contrib import admin
from django.urls import path
from webliniber import views
from webliniber.api_views import animales_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('animales', views.animales, name='animales'),
    path('get_animals', animales_api.get_animals, name='get_animals')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
