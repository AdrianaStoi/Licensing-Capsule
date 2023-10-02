from . import views
from django.urls import path

urlpatterns = [
    path('base.html/', views.basePreview, name='base.html'),
]
