from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('contact/', views.contact_us, name='contact_us'),
    path('faq/', views.faq, name='faq'),
    path('help/', views.help_center, name='help_center'),
    path('language/change/', views.change_language, name='change_language'),
    path('language/<str:language_code>/', views.set_language_from_url, name='set_language'),
    path('language-demo/', views.language_demo, name='language_demo'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:token>/', views.password_reset_confirm, name='password_reset_confirm'),
]
