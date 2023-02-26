from django.urls import path
from . import views

app_name = 'parent_ally'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.delete_posting, name='delete'),
    path('create/', views.create_posting, name='create-posting')
]
