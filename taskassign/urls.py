from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = "home_page"),
    path('add/', TaskView.as_view(), name = 'task_add'),
    path('<int:id>/detail/', task_detail, name = "task_detail")
]