"""Urls for triptales app"""

from django.conf.urls import include
from django.urls import path
from triptales import views

app_name = 'triptales'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('goto/', views.goto_url, name='goto'),
    path('quiz', views.quiz, name='quiz'),
    path('basetest', views.basetest, name='basetest'),
    path('basetest/<str:continent>', views.basetest, name='basetest'),
    path('posts/<str:continent_name>/', views.posts_by_continent, name='posts_by_continent'),
    path('posts/detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('add_country/', views.add_country, name='add_country'),
    path('add_location/', views.add_location, name='add_location')
]
