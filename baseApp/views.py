from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Post
# Create your views here.
@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'baseApp/home.html', context)


def log_out(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'baseApp/login_form.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'baseApp/register_form.html', context)

