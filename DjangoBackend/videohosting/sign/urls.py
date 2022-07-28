from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', RegisterView.as_view()),
]
