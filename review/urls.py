from . import views
from django.urls import path, include
from .views import filter_games

urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
    path('<slug:game>/<slug:review>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:game>/<slug:review>', views.ReviewLike.as_view(), name='review_like'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('filter/', filter_games, name='filter_games'),
]                              
