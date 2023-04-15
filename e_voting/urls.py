"""e_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from site_content.views import HomeView, LandingPage

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('user_management.urls')),
    path('user/', include('user_management.urls')),
    # path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('', LandingPage.as_view(), name='home_1'),
    path('site/', include('site_content.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),

    # path('password-reset/', PasswordResetView.as_view()),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
