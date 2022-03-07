from django.conf.urls.static import static
from django.urls import path, include

from online_store_hakaton import settings
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view()),
]