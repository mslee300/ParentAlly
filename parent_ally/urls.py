from django.urls import path
from . import views

app_name = 'parent_ally'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.view_posts_list, name='list'),
    path('detail/<int:pk>/', views.view_post, name='detail'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('delete-comment/<int:pk>',
         views.delete_comment,
         name='delete-comment'),
    path('create-post/', views.create_post, name='create-posting'),
]
