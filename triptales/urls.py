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
]
