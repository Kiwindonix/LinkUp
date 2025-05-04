from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('news/', views.news_view, name='news'),
    path('profile/', lambda request: HttpResponse("Профіль (тимчасово)"), name='profile'),
    path('calendar/', lambda request: HttpResponse("Календар (тимчасово)"), name='calendar_redirect'),
    path('gallery/', lambda request: HttpResponse("Галерея (тимчасово)"), name='gallery'),
    path('search/', views.search_contacts, name='search_contacts'),
    path('create/', views.create_post, name='create_post'),
]
