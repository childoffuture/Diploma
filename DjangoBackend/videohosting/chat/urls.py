from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', ChatView.as_view())
]
