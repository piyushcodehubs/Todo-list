from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('tasks/',views.add_task,name='add_task'),
    path('delete_taks/<int:id>/',views.delete_taks,name='delete_taks'),
    path('edit/<int:id>/',views.edit_task,name='edit_task'),
]