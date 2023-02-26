from django.urls import path
from . import views

app_name = 'parent_ally'
urlpatterns = [
    path('', views.view_posts_list, name='index'),
    path('assistance/', views.view_assistance_list),
    path('programs/', views.view_programs_list),
    path('connect/', views.view_connect_list),
    path('list/', views.view_posts_list, name='list'),
    path('detail/<int:pk>/', views.view_post, name='detail'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('delete-comment/<int:pk>',
         views.delete_comment,
         name='delete-comment'),
    path('create-post/', views.create_post, name='create-posting'),
    path('edit-comment/<int:pk>/', views.edit_comment, name='edit-comment'),
    path('new/', views.new_post),
    path('details1/', views.details_1),
    path('details5/', views.details_5),
    path('details7/', views.details_7),
]
