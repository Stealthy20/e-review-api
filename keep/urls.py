from django.urls import path
from keep import views

urlpatterns = [
    path('keep/', views.KeepList.as_view()),
    path('keep/<int:pk>/', views.KeepDetail.as_view()),
]