from django.urls import path
from .views import UserInfoView

urlpatterns = [
    path('user/', UserInfoView.as_view(), name='user_info'),
]
