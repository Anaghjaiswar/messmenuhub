from django.urls import path
from . import views

app_name = 'owners'

urlpatterns = [
    # Basic pages views (HTML rendering views)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage-menu/', views.manage_menu, name='manage_menu'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('menu-posting/', views.menu_posting, name='menu_posting'),
    path('resources/', views.resources, name='resources'),
    path('resources/special-offers-promotions/', views.special_offers_promotions, name='promotions'),
    path('resources/help-guidelines/', views.help_guidelines, name='help_guidelines'),
    path('resources/contact-support/', views.contact_support, name='contact_support'),
    path('resources/announcements/', views.announcements, name='announcements'),

    # API endpoints for login/signup (JWT authentication)
    path('api/signup/', views.SignupView.as_view(), name='signup_api'),
    path('api/login/', views.LoginView.as_view(), name='login_api'),
]
