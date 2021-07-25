from django.urls import path
from rest_framework import views
from . import views

urlpatterns = [
    path('gettype/', views.getType.as_view()),
    path('createForm/',  views.createForm.as_view()),
    path('createQuestion/',  views.createQuestion.as_view()),
    path('editQuestion/<str:pk>', views.editQuestion.as_view()),
    path('createResponse/',views.createResponse.as_view()),
    path('editUserResponse/<str:pk>', views.editUserResponse.as_view()),
]