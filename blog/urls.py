from django.urls import path 
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='post'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    # path('post/new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.BlogEdit.as_view(), name='edit'),
]