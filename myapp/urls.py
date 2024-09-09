
from django.urls import path
from .import views
urlpatterns = [
    path('', views.task_list,name="home"),
    path('task_update/<int:pe>/', views.task_update,name="task_update"),
    path('task_delete/<int:pd>/', views.task_delete,name="task_delete"),



]



