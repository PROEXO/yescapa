from django.urls import path
from .views import *
urlpatterns = [
    path('level1', my_engine_level1),
    path('level2', my_engine_level2),
    path('level3', my_engine_level3)
]