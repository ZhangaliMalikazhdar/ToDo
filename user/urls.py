from django.urls import path

from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path('auth/', CustomAuthToken.as_view()),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', Logout.as_view()),
    path("password_reset", password_reset_request, name="password_reset")
]
