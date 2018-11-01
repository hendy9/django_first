from django.urls import path, include
from . import views




urlpatterns = [
    #path("", views.index, name="moviebook_index"),
    path("",views.index,name="filmovy_index"),

]
