from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
     path('login/', views.signup, name='login'),
      path('rules/', views.rules, name='rules'),
       path('logout/', views.logout, name='logout'),
       path('quiz/', views.quiz, name='quiz'),
       path('end/', views.endexm, name='endexm'),
]