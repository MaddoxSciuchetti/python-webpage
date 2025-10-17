# url patterns for this handyman project
from django.urls import path
from . import views

app_name = 'handyman'

urlpatterns = [
    path('',views.index, name='index'),
    #page that shows all topics:
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name="topic"),
]

