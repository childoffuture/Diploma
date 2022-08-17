from django.urls import path, include
from .views import *

urlpatterns = [
    path('', DrfBaseView.as_view()),
    path('subscriptions', DrfSubscriptionView.as_view()),
    path('recommendations', DrfRecommendView.as_view()),
    path('myvideos', DrfMyVideoView.as_view()),
    path('watch/<int:pk>', DrfVideoView.as_view()),
]
