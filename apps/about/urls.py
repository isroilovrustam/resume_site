from django.urls import path
from .views import index, about, credential

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('credential/', credential, name='credential')
]
