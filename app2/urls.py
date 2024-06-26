from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('api/drinks', drink_list),
    path('api/drinks/<int:id>', drink_detail),
    # path('api/livreurs', livreur_list),
    # path('api/livreurs/<int:id>', livreur_detail),
    # path('api/clients', clients_list),
    # path('api/clients/<int:id>', clients_detail),
    path('api/gestionaires', gestionaires_list),
    path('api/gestionaires/<int:id>', gestionaires_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
