from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Booking
from .forms import BookingForm
from accounts.models import LoginOTP


class OTPRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        if not LoginOTP.objects.filter(user=request.user, is_verified=True).exists():
            return redirect("verify_otp")

        return super().dispatch(request, *args, **kwargs)



class BookingListView(OTPRequiredMixin, LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreateView(OTPRequiredMixin, LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/form.html'
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookingUpdateView(OTPRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/form.html'
    success_url = reverse_lazy('booking_list')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingDeleteView(OTPRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking/delete.html'
    success_url = reverse_lazy('booking_list')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
