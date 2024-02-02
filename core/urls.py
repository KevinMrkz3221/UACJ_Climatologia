from django.urls import path, include

# URLS
urlpatterns = [
    path('account/', include('core.authenticate.urls')),
    path('estaciones/', include('core.estacion.urls'))
]