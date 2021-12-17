from django.urls import path
from todolist_app import views


urlpatterns = [
    path('', views.todolist, name = 'todolist'),
    path('delete/<task_id>',views.delete_task, name="delete_task"),
    path('update/<task_id>', views.update_task, name="update_task"),
    path('complete/<task_id>',views.complete_task, name="complete_task"),
    path('uncompleted/<task_id>',views.uncompleted_task, name="uncompleted_task"),
]
