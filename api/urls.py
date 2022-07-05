from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', ListTable.as_view()),
    path('todo/<int:pk>/', DetailTask.as_view()),
    path('todo/<int:pk>/execute/', ClickDone.as_view()),
]
