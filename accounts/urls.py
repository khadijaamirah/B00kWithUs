from django.urls import path
from . import views

urlpatterns = [
    # Authentication & OTP
    path('login/', views.login_with_otp, name='login'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # User profile
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('change-password/', views.change_password_view, name='change_password'),

    # Secure Backend API
    path('api/secure-booking/', views.secure_booking_api, name='secure_booking_api'),
]

