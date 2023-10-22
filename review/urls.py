from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
    path('<slug:game>/<slug:review>/', views.ReviewDetail.as_view(), name='review_detail'),
]                              
