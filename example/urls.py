from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('create', views.PersonCreateView.as_view(), name='create'),
    path('my-text/<int:pk>/', views.MyTextDetailView.as_view(), name='mytext_detail'),
    path('person/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
]
