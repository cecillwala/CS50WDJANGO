from django.urls import path
from . import views

app_name = "valentines"
urlpatterns = [
    path("", views.index, name="index")
]