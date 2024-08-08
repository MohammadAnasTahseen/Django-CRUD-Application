from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.home,name="home"),
    # path("home/",views.home,name="home"),
    path("add_student/",views.add_student),
    path("delete_student/<int:roll>",views.delete_student),
    path("update_student/<int:roll>",views.update_student),
    path("do_update_student/<int:roll>",views.do_update_student),
]