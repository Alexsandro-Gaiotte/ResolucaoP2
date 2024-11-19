from django.contrib import admin
from django.urls import path
from todos.views import TodoListView

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
 path('', TodoListView.as_view(), name='todo_list')
]
