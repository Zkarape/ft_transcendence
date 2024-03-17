"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from src import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('users/', views.get_users),
	path('register/', views.register),
	path('login/', views.login),
	path('login_intra/', views.login_intra),
	path('signin/', views.signin),
	path('login_page/', views.login_page),
	path('auth_qr/', views.auth_qr),
	# path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
	# path('get_students/', views.get_students),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
