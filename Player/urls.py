from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('accounts.urls')),
    path('', include('app_player.urls'))

]
