from django.urls import path
from .views import recipe_list, home

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
]
