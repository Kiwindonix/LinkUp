from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home_view, name='home'),
    path('news/', views.news_view, name='news'),
    path('profile/', lambda request: HttpResponse("Профіль (тимчасово)"), name='profile'),
    path('calendar/', lambda request: HttpResponse("Календар (тимчасово)"), name='calendar_redirect'),
    path('gallery/', lambda request: HttpResponse("Галерея (тимчасово)"), name='gallery'),
]
