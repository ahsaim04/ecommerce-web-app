from django.urls import path

from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('login/',auth_views.LoginView.as_view(template_name='store/login.html',authentication_form=LoginForm),name='login'),
	path('accounts/profile/', views.store, name="store"),
	path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]