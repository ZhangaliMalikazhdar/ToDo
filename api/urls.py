from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', list_all_tasks),
    path('todo/<int:pk>/', get_task),
    path('todo/<int:pk>/execute/', click_done),

]
