from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.welcome),
    path('sign_up', views.sign_up),
    path('user_login', views.user_login, name='login'),
    path('profile/', views.profile),
    path('user_logout/', views.user_logout, name='logout'),
    path('changepass', views.changepass),
]