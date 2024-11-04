# views.py
from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from .models import NewsletterSubscription 

@csrf_exempt  #
def subscribe(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        name = request.POST.get('name')

    

        return JsonResponse({'msg': 'Thank you for subscribing!'}, status=200)  

    return render(request, 'newsletter.html') 
