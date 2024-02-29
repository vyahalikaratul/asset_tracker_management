
from django.urls import path
from django.contrib.auth import views as auth_views
from authentication.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='admin_login'),
]
