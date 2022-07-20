from django.urls import path
from .views import *

urlpatterns = [
    path('', BaseView.as_view()),
    path('subscriptions', SubscriptionView.as_view()),
    path('recommendations', RecommendView.as_view()),
    path('myvideos', MyVideoView.as_view()),
    path('add', AddView.as_view()),
    path('watch/<int:pk>', VideoView.as_view())
]
