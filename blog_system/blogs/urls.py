from django.urls import path

from . import views

urlpatterns = (
    path('', views.BlogsListView.as_view(), name='index'),
    path('<int:pk>/', views.BlogDetailsView.as_view(), name='blog details'),
    path('<int:pk>/<slug:slug>/', views.BlogDetailsView.as_view(), name='blog details'),
    path('create/', views.CreateBlogView.as_view(), name='create blog'),
)
