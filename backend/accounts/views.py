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

def user_profil(request):
    user_profil = request.user
    context = {
        'user_profil': user_profil,
    }
    return render(request, 'accounts/user_profil.html', context)

def user_profil_view(request, username):
    User = settings.AUTH_USER_MODEL
    user_profil = User.objects.get(username=username)

    context = {
        'user_profil': user_profil
    }
    return render(request, 'accounts/user_profil.html', context)