from django.urls import path
from app3 import views

urlpatterns = [
    path('<data>/',views.index3,name = "index3"),
]
