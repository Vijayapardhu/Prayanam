from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Payment, PaymentGateway, Refund, PaymentMethod, PaymentTransaction
from bookings.models import Booking
from datetime import datetime
import json
import random
import string

@login_required
def payment_list(request):
    """Display user's payment history"""
    payments = Payment.objects.filter(user=request.user).order_by('-created_at')
    
    # Calculate statistics
    total_payments = payments.count()
    successful_payments = payments.filter(payment_status='completed').count()
    failed_payments = payments.filter(payment_status='failed').count()
    total_amount = sum(payment.amount for payment in payments if payment.payment_status == 'completed')
    
    context = {
        'payments': payments,
        'total_payments': total_payments,
        'successful_payments': successful_payments,
        'failed_payments': failed_payments,
        'total_amount': total_amount,
    }
    return render(request, 'payments/payment_list.html', context)

@login_required
def payment_detail(request, payment_id):
    """Display payment details"""
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)
    
    context = {
        'payment': payment,
    }
    return render(request, 'payments/payment_detail.html', context)

@login_required
def payment_success(request, payment_id):
    """Display payment success page"""
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)
    booking = payment.booking
    package = booking.package if booking else None
    
    # Debug information
    print(f"🔍 Payment Success Debug:")
    print(f"   Payment ID: {payment.id}")
    print(f"   Payment Amount: {payment.amount}")
    print(f"   Payment Method: {payment.payment_method}")
    print(f"   Booking ID: {booking.id if booking else 'None'}")
    print(f"   Package ID: {package.id if package else 'None'}")
    print(f"   Package Name: {package.name if package else 'None'}")
    print(f"   Booking From Date: {booking.from_date if booking else 'None'}")
    print(f"   Booking To Date: {booking.to_date if booking else 'None'}")
    print(f"   Booking Members Count: {booking.members_count if booking else 'None'}")
    
    context = {
        'payment': payment,
        'booking': booking,
        'package': package,
        'user': request.user,
    }
    return render(request, 'payments/payment_success.html', context)

@login_required
def process_payment(request, booking_id):
    """Process payment for a booking with test payment methods"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'GET':
        # Display payment form with test payment methods
        context = {
            'booking': booking,
            'test_payment_methods': [
                {
                    'id': 'test_credit_card',
                    'name': 'Test Credit Card',
                    'icon': 'fas fa-credit-card',
                    'description': 'Visa/MasterCard (Test Mode)',
                    'test_cards': [
                        {'number': '4111111111111111', 'expiry': '12/25', 'cvv': '123', 'name': 'Test Visa'},
                        {'number': '5555555555554444', 'expiry': '12/25', 'cvv': '123', 'name': 'Test MasterCard'},
                    ]
                },
                {
                    'id': 'test_debit_card',
                    'name': 'Test Debit Card',
                    'icon': 'fas fa-credit-card',
                    'description': 'Debit Card (Test Mode)',
                    'test_cards': [
                        {'number': '4000000000000002', 'expiry': '12/25', 'cvv': '123', 'name': 'Test Debit'},
                    ]
                },
                {
                    'id': 'test_upi',
                    'name': 'Test UPI',
                    'icon': 'fas fa-mobile-alt',
                    'description': 'UPI Payment (Test Mode)',
                    'test_upi_ids': [
                        'test@paytm',
                        'test@phonepe',
                        'test@googlepay',
                    ]
                },
                {
                    'id': 'test_net_banking',
                    'name': 'Test Net Banking',
                    'icon': 'fas fa-university',
                    'description': 'Internet Banking (Test Mode)',
                    'test_banks': [
                        'State Bank of India',
                        'HDFC Bank',
                        'ICICI Bank',
                        'Axis Bank',
                    ]
                },
                {
                    'id': 'test_wallet',
                    'name': 'Test Digital Wallet',
                    'icon': 'fas fa-wallet',
                    'description': 'Digital Wallet (Test Mode)',
                    'test_wallets': [
                        'Paytm Wallet',
                        'PhonePe Wallet',
                        'Google Pay',
                        'Amazon Pay',
                    ]
                }
            ]
        }
        return render(request, 'payments/process_payment.html', context)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(f"Received payment data: {data}")  # Debug log
            
            action = data.get('action', 'process_payment')
            payment_method_type = data.get('payment_method_type')
            otp = data.get('otp')
            
            # Handle OTP actions
            if action == 'send_otp':
                return send_otp(request, booking, payment_method_type)
            elif action == 'verify_otp':
                return verify_otp_and_process_payment(request, booking, payment_method_type, otp, data)
            
            return JsonResponse({
                'success': False,
                'error': 'Invalid action'
            })
            
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON data'
            })
        except Exception as e:
            print(f"Payment processing error: {e}")
            return JsonResponse({
                'success': False,
                'error': 'Payment processing failed'
            })

@login_required
def payment_methods(request):
    """Display user's payment methods"""
    payment_methods = PaymentMethod.objects.filter(user=request.user).order_by('-is_default', '-created_at')
    recent_transactions = PaymentTransaction.objects.filter(
        payment__user=request.user
    ).order_by('-created_at')[:5]
    
    context = {
        'payment_methods': payment_methods,
        'recent_transactions': recent_transactions,
    }
    return render(request, 'payments/payment_methods.html', context)

@login_required
def add_payment_method(request):
    """Add a new payment method"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            payment_type = data.get('payment_type')
            
            # Create payment method based on type
            if payment_type == 'credit_card':
                payment_method = PaymentMethod.objects.create(
                    user=request.user,
                    payment_type='credit_card',
                    card_last4=data.get('card_last4'),
                    card_expiry_month=data.get('card_expiry_month'),
                    card_expiry_year=data.get('card_expiry_year'),
                    card_brand=data.get('card_brand'),
                    is_default=data.get('is_default', False)
                )
            elif payment_type == 'debit_card':
                payment_method = PaymentMethod.objects.create(
                    user=request.user,
                    payment_type='debit_card',
                    card_last4=data.get('card_last4'),
                    card_expiry_month=data.get('card_expiry_month'),
                    card_expiry_year=data.get('card_expiry_year'),
                    card_brand=data.get('card_brand'),
                    is_default=data.get('is_default', False)
                )
            elif payment_type == 'upi':
                payment_method = PaymentMethod.objects.create(
                    user=request.user,
                    payment_type='upi',
                    upi_id=data.get('upi_id'),
                    is_default=data.get('is_default', False)
                )
            elif payment_type == 'net_banking':
                payment_method = PaymentMethod.objects.create(
                    user=request.user,
                    payment_type='net_banking',
                    bank_name=data.get('bank_name'),
                    account_last4=data.get('account_last4'),
                    ifsc_code=data.get('ifsc_code'),
                    is_default=data.get('is_default', False)
                )
            elif payment_type == 'wallet':
                payment_method = PaymentMethod.objects.create(
                    user=request.user,
                    payment_type='wallet',
                    wallet_name=data.get('wallet_name'),
                    wallet_number=data.get('wallet_number'),
                    is_default=data.get('is_default', False)
                )
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid payment type'
                })
            
            # If this is set as default, unset others
            if payment_method.is_default:
                PaymentMethod.objects.filter(user=request.user).exclude(id=payment_method.id).update(is_default=False)
            
            return JsonResponse({
                'success': True,
                'message': 'Payment method added successfully',
                'payment_method_id': payment_method.id
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    })

@login_required
def delete_payment_method(request, method_id):
    """Delete a payment method"""
    try:
        payment_method = get_object_or_404(PaymentMethod, id=method_id, user=request.user)
        payment_method.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Payment method deleted successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@login_required
def refund_request(request, payment_id):
    """Request a refund for a payment"""
    payment = get_object_or_404(Payment, id=payment_id, user=request.user)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reason = data.get('reason', '')
            
            # Create refund request
            refund = Refund.objects.create(
                payment=payment,
                amount=payment.amount,
                reason=reason,
                refund_status='pending'
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Refund request submitted successfully',
                'refund_id': refund.id
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    })

@login_required
def transaction_history(request):
    """Display transaction history"""
    transactions = PaymentTransaction.objects.filter(
        payment__user=request.user
    ).order_by('-created_at')
    
    context = {
        'transactions': transactions,
    }
    return render(request, 'payments/transaction_history.html', context)

@login_required
def payment_gateway_status(request):
    """Get payment gateway status"""
    gateways = PaymentGateway.objects.all()
    gateway_status = []
    
    for gateway in gateways:
        gateway_status.append({
            'id': gateway.id,
            'name': gateway.name,
            'status': 'online',
            'response_time': '0.2s'
        })
    
    return JsonResponse({'gateways': gateway_status})

def send_otp(request, booking, payment_method_type):
    """Send OTP to user's email for payment verification"""
    try:
        # Generate 6-digit OTP
        otp = ''.join(random.choices(string.digits, k=6))
        
        # Store OTP and payment method type in session
        request.session['payment_otp'] = otp
        request.session['payment_booking_id'] = booking.id
        request.session['payment_method_type'] = payment_method_type
        request.session['payment_data'] = {
            'booking_id': booking.id,
            'amount': float(booking.total_price),
            'payment_method_type': payment_method_type,
            'timestamp': datetime.now().isoformat()
        }
        
        # Send OTP email
        try:
            from utils.email_service import EmailService
            EmailService.send_otp_email(request.user.email, otp, booking, payment_method_type)
        except Exception as email_error:
            print(f"Failed to send OTP email: {email_error}")
            # For demo purposes, we'll still return success even if email fails
        
        return JsonResponse({
            'success': True,
            'message': f'OTP sent successfully to {request.user.email}',
            'otp_hint': f'Test OTP: {otp}'  # Only for testing - remove in production
        })
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return JsonResponse({
            'success': False,
            'error': 'Failed to send OTP'
        })

def verify_otp_and_process_payment(request, booking, payment_method_type, otp, payment_data):
    """Verify OTP and process payment with test payment methods"""
    try:
        # Verify OTP
        stored_otp = request.session.get('payment_otp')
        stored_booking_id = request.session.get('payment_booking_id')
        stored_payment_method_type = request.session.get('payment_method_type')
        
        print(f"🔍 OTP Verification Debug:")
        print(f"   Stored OTP: {stored_otp}")
        print(f"   Provided OTP: {otp}")
        print(f"   Stored Booking ID: {stored_booking_id}")
        print(f"   Current Booking ID: {booking.id}")
        print(f"   Stored Payment Method: {stored_payment_method_type}")
        print(f"   Current Payment Method: {payment_method_type}")
        
        if not stored_otp or not stored_booking_id or stored_booking_id != booking.id:
            print("❌ Invalid or expired OTP session")
            return JsonResponse({
                'success': False,
                'error': 'Invalid or expired OTP session'
            })
        
        if stored_payment_method_type != payment_method_type:
            print("❌ Payment method mismatch")
            return JsonResponse({
                'success': False,
                'error': 'Payment method mismatch'
            })
        
        if otp != stored_otp:
            print("❌ Invalid OTP")
            return JsonResponse({
                'success': False,
                'error': 'Invalid OTP'
            })
        
        print("✅ OTP verification successful")
        
        # Clear OTP from session
        request.session.pop('payment_otp', None)
        request.session.pop('payment_booking_id', None)
        request.session.pop('payment_method_type', None)
        request.session.pop('payment_data', None)
        
        # Clean up any previous failed payment attempts for this booking
        Payment.objects.filter(booking=booking, payment_status='failed').delete()
        
        # Check if payment already exists for this booking
        existing_payment = Payment.objects.filter(booking=booking, payment_status='completed').first()
        if existing_payment:
            return JsonResponse({
                'success': False,
                'error': 'Payment already completed for this booking'
            })
        
        # Process payment based on payment method type
        payment_result = process_test_payment(booking, payment_method_type, payment_data)
        
        if payment_result['success']:
            # Create payment record with error handling
            try:
                payment = Payment.objects.create(
                    user=request.user,
                    booking=booking,
                    amount=booking.total_price,
                    payment_method=payment_method_type,
                    payment_status='completed',
                    transaction_id=payment_result['transaction_id'],
                    completed_at=datetime.now(),
                    gateway_response=payment_result['gateway_response']
                )
            except Exception as e:
                print(f"Error creating payment record: {e}")
                return JsonResponse({
                    'success': False,
                    'error': 'Failed to create payment record. Please try again.'
                })
            
            # Update booking status
            booking.status = 'confirmed'
            booking.save()
            
            # Create transaction log
            PaymentTransaction.objects.create(
                payment=payment,
                action='payment_completed',
                amount=booking.total_price,
                status='success',
                gateway_response=payment_result['gateway_response']
            )
            
            # Send payment confirmation email
            try:
                from utils.email_service import EmailService
                EmailService.send_payment_confirmation(payment)
            except Exception as email_error:
                print(f"Failed to send payment confirmation email: {email_error}")
            
            return JsonResponse({
                'success': True,
                'payment_id': payment.id,
                'transaction_id': payment_result['transaction_id'],
                'message': 'Payment processed successfully',
                'redirect_url': f'/payments/success/{payment.id}/'
            })
        else:
            # Create failed payment record
            payment = Payment.objects.create(
                user=request.user,
                booking=booking,
                amount=booking.total_price,
                payment_method=payment_method_type,
                payment_status='failed',
                failure_reason=payment_result['error']
            )
            
            PaymentTransaction.objects.create(
                payment=payment,
                action='payment_failed',
                amount=booking.total_price,
                status='failed',
                gateway_response={'error': payment_result['error']}
            )
            
            return JsonResponse({
                'success': False,
                'error': payment_result['error']
            })
            
    except Exception as e:
        print(f"Error verifying OTP: {e}")
        return JsonResponse({
            'success': False,
            'error': 'Failed to verify OTP and process payment'
        })

def process_test_payment(booking, payment_method_type, payment_data):
    """Process test payment based on payment method type"""
    try:
        # Simulate payment processing delay
        import time
        time.sleep(1)  # Simulate network delay
        
        # Generate unique transaction ID with microsecond precision
        import uuid
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')  # Include microseconds
        unique_id = str(uuid.uuid4())[:8]  # First 8 characters of UUID
        transaction_id = f"TXN_{booking.id}_{timestamp}_{unique_id}"
        
        # Ensure transaction ID is unique by checking database
        while Payment.objects.filter(transaction_id=transaction_id).exists():
            unique_id = str(uuid.uuid4())[:8]
            transaction_id = f"TXN_{booking.id}_{timestamp}_{unique_id}"
        
        # Process based on payment method type
        if payment_method_type == 'test_credit_card':
            card_number = payment_data.get('card_number', '')
            card_expiry = payment_data.get('card_expiry', '')
            card_cvv = payment_data.get('card_cvv', '')
            
            # Validate test card details
            if not card_number or not card_expiry or not card_cvv:
                return {
                    'success': False,
                    'error': 'Invalid card details'
                }
            
            # Simulate card validation
            if len(card_number) < 13 or len(card_number) > 19:
                return {
                    'success': False,
                    'error': 'Invalid card number'
                }
            
            if len(card_cvv) < 3 or len(card_cvv) > 4:
                return {
                    'success': False,
                    'error': 'Invalid CVV'
                }
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'gateway_response': {
                    'status': 'success',
                    'message': 'Credit card payment processed successfully',
                    'card_last4': card_number[-4:],
                    'card_brand': 'Visa' if card_number.startswith('4') else 'MasterCard',
                    'auth_code': f"AUTH{random.randint(100000, 999999)}"
                }
            }
            
        elif payment_method_type == 'test_debit_card':
            card_number = payment_data.get('card_number', '')
            card_expiry = payment_data.get('card_expiry', '')
            card_cvv = payment_data.get('card_cvv', '')
            
            if not card_number or not card_expiry or not card_cvv:
                return {
                    'success': False,
                    'error': 'Invalid card details'
                }
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'gateway_response': {
                    'status': 'success',
                    'message': 'Debit card payment processed successfully',
                    'card_last4': card_number[-4:],
                    'card_brand': 'Debit',
                    'auth_code': f"AUTH{random.randint(100000, 999999)}"
                }
            }
            
        elif payment_method_type == 'test_upi':
            upi_id = payment_data.get('upi_id', '')
            
            if not upi_id or '@' not in upi_id:
                return {
                    'success': False,
                    'error': 'Invalid UPI ID'
                }
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'gateway_response': {
                    'status': 'success',
                    'message': 'UPI payment processed successfully',
                    'upi_id': upi_id,
                    'reference_id': f"UPI{random.randint(100000000, 999999999)}"
                }
            }
            
        elif payment_method_type == 'test_net_banking':
            bank_name = payment_data.get('bank_name', '')
            account_number = payment_data.get('account_number', '')
            
            if not bank_name or not account_number:
                return {
                    'success': False,
                    'error': 'Invalid bank details'
                }
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'gateway_response': {
                    'status': 'success',
                    'message': 'Net banking payment processed successfully',
                    'bank_name': bank_name,
                    'account_last4': account_number[-4:],
                    'reference_id': f"NB{random.randint(100000000, 999999999)}"
                }
            }
            
        elif payment_method_type == 'test_wallet':
            wallet_name = payment_data.get('wallet_name', '')
            wallet_number = payment_data.get('wallet_number', '')
            
            if not wallet_name or not wallet_number:
                return {
                    'success': False,
                    'error': 'Invalid wallet details'
                }
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'gateway_response': {
                    'status': 'success',
                    'message': 'Digital wallet payment processed successfully',
                    'wallet_name': wallet_name,
                    'wallet_number': wallet_number,
                    'reference_id': f"WLT{random.randint(100000000, 999999999)}"
                }
            }
            
        else:
            return {
                'success': False,
                'error': 'Unsupported payment method'
            }
            
    except Exception as e:
        print(f"Test payment processing error: {e}")
        return {
            'success': False,
            'error': 'Payment processing failed'
        }
