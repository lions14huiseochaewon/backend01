from django.contrib import admin
from django.urls import path
from .views import * #작성한 view import

app_name='deskresearch'
urlpatterns=[
    path('',home,name='home'),
    path('post/<int:post_id>', detail, name='detail'),
    path('new/',new,name='new'),
    path('create/',create,name="create"),
    path('delete/<int:post_id>',delete,name="delete"),
    path('update/<int:post_id>',update_page,name="update_page"),
    path('update_post/<int:post_id>',update_post,name="update_post"),
    path('<int:post_id>/comment',add_comment,name='add_comment'),
]
