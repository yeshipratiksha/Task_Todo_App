from  django.urls import path 
from .import views
urlpatterns = [
    
    path('',views.Add_task,name='home'),
    path('update-task/<str:pk>/',views.update_task,name='update-task'),
    path('delete-task/<str:pk>/',views.delete_task,name='delete-task'),
]
