from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import authenticate, login
# Create your views here.

def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == "POST":
        user = authenticate(
            request, username=username, password=password
        )
        
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            return redirect("home:index")
    return render(request, 'accounts/user_login.html', {})