from django.urls import path
from . import views 
from django.http import HttpResponse
from auth_system.views import ProfileView, update_profile

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('news/', views.news_view, name='news'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('calendar/', lambda request: HttpResponse("Календар (тимчасово)"), name='calendar_redirect'),
    path('gallery/', lambda request: HttpResponse("Галерея (тимчасово)"), name='gallery'),
    path('create/', views.create_post, name='create_post'),
    path("update-profile/", update_profile, name="update_profile"),
    path('search/', views.search_posts, name='search_posts'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),

]
