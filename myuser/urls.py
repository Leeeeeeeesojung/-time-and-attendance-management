from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register ),
    path('login/', views.login  ),
    path('logout/', views.logout  ),
    # path('lunch/', views.lunch ),
    path('upload/', views.upload ),
    path('face/', views.face),
]
