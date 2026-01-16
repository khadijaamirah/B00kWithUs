from django.urls import path
from . import views
from .api import secure_booking_api

urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking_list'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),

    path('api/secure-booking/', secure_booking_api),
]
