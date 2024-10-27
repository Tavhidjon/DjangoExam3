from django.urls import path
from .views import *

urlpatterns = [
    path("",get_all,name="get"),
    path("add",add,name="add"),
    path("edit/<int:pk>",edit,name="edit"),
    path("delete/<int:pk>",delete,name="delete")
]
