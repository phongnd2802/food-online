from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def register_user(request):
    return render(request, 'accounts/register-user.html')
