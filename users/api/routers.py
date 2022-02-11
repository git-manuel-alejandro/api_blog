from django.urls import path
from users.api.views import RegisterView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)


urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me', UserView.as_view(), name='UserView'),
]
