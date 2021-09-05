from django.urls import path
from .views import (
    MyView,
    UserCreateView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('my_view/', MyView.as_view(), name='my_view'),
    path('user_create_view/', UserCreateView.as_view(), name='user_create_view')
]