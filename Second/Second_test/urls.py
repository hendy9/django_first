from django.urls import path, include
from . import views




urlpatterns = [
    #path("", views.index, name="moviebook_index"),
    path("",views.index,name="filmovy_index"),
    path("form/", views.form_name_view,name='form_name'),

]
