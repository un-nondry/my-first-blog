from django.urls import path 
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='post'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('create/', views.BlogCreate.as_view(), name='create'),
    path('<int:pk>/edit/', views.BlogEdit.as_view(), name='edit'),
    path('tag/<int:pk>/', views.BlogTag.as_view(), name='tag'),
]