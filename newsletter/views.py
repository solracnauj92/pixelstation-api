from django.shortcuts import render
from django.views import View


class NewsletterSubscriptionView(View):
    def get(self, request):
        
        return render(request, 'newsletter/subscribe.html')

    def post(self, request):
        
        return render(request, 'newsletter/success.html')

#
def subscribe(request):
    if request.method == 'POST':
       
        return render(request, 'newsletter/success.html')
    return render(request, 'newsletter/subscribe.html')
