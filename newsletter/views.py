from django.shortcuts import render
from django.http import JsonResponse
import re
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings

def validate_email(request): 
    if request.method == 'POST':
        email = request.POST.get("email", None)
        if email is None:
            return JsonResponse({'msg': 'Email is required.'}, status=400)

        # Check if email already exists
        if SubscribedUsers.objects.filter(email=email).exists():
            return JsonResponse({'msg': 'Email Address already exists'}, status=400)

        # Validate email format
        if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
            return JsonResponse({'msg': 'Invalid Email Address'}, status=400)

        return JsonResponse({'msg': ''}, status=200)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get("email", None)
        name = request.POST.get("name", None)
        
        # Validate input
        if not email or not name:
            return JsonResponse({'msg': 'Name and Email are required.'}, status=400)

        # Create a new subscription
        subscribed_user = SubscribedUsers(email=email, name=name)
        subscribed_user.save()

        # Send a confirmation email
        subject = 'Newsletter Subscription'
        message = f'Hello {name}, Thanks for subscribing! You will receive notifications of the latest articles on our website.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

        return JsonResponse({'msg': 'Thanks. Subscribed Successfully!'}, status=200)

    return JsonResponse({'msg': 'Invalid request method.'}, status=405)