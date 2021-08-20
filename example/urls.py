from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('my-text/<int:pk>/', views.MyTextDetailView.as_view(), name='mytext_detail'),
]
