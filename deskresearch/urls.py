from django.urls import path
from .views import *

app_name = 'deskresearch'

urlpatterns=[
    path('',PostListView.as_view()),
    path('<int:pk>/',PostDetailView.as_view()),
    path('records/',RecordView.as_view()),

]
