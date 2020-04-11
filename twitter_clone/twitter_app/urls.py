from django.urls import path

from . import views

app_name= "twitter_app"
urlpatterns = [
    path('', views.TweetListView.as_view(), name='home_page'),
    path('twitter/<int:pk>/', views.TweetDetailView.as_view(), name='detail'),
    path('twitter/new_post/', views.TweetCreateView.as_view(), name='new_post'),
     path('twitter/<int:pk>/delete/', views.TweetDeleteView.as_view(), name='delete'),
]