from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_index, name='feedback_index'),
    path('feedback_user/', views.feedback_index_user, name='feedback_index_user'),
]
