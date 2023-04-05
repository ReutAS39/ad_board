from django.urls import path

from users import views
from users.views import UserRegister, UserLogin, logout_user

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]