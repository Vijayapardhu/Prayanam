from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('<int:payment_id>/', views.payment_detail, name='payment_detail'),
    path('process/<int:booking_id>/', views.process_payment, name='process_payment'),
    path('success/<int:payment_id>/', views.payment_success, name='payment_success'),
    path('methods/', views.payment_methods, name='payment_methods'),
    path('methods/add/', views.add_payment_method, name='add_payment_method'),
    path('methods/<int:method_id>/delete/', views.delete_payment_method, name='delete_payment_method'),
    path('<int:payment_id>/refund/', views.refund_request, name='refund_request'),
    path('transactions/', views.transaction_history, name='transaction_history'),
    path('gateway-status/', views.payment_gateway_status, name='gateway_status'),
]
