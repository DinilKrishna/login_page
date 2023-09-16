from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.cache import cache_control, never_cache
from django.contrib import messages


# Create your views here.

@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def login_page(request):
    if 'username' in request.session:
        return redirect(home_page)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            request.session['username'] = username
            return redirect('home_page')
        else:
            try:
                user = User.objects.get(username=username)
                messages.error(request, 'Password Incorrect', extra_tags='invalid-login')
            except User.DoesNotExist:
                messages.error(request, 'Invalid Username', extra_tags='invalid-login')

            # messages.error(request, 'invalid username or password', extra_tags='invalid-login')
    return render(request, 'login.html')

@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def signup_page(request):
    if 'username' in request.session:
        return render (request, 'home.html')
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        
        if User.objects.filter(username=uname).exists():
            messages.warning(request, 'Username already exist')
        

        
        elif pass1 !=pass2:
            messages.error(request, "Passwords doesn't match", extra_tags='invalid-login')
        
        
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login_page')


    return render(request, 'signup.html')


@cache_control(no_cache = True, must_revalidate = True, no_store = True)
@never_cache
def home_page(request):
    if 'username' in request.session:
        return render (request, 'home.html')
    return redirect(login_page)

def logout_page(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login_page')
