from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PostForm
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
@login_required
def home(request):
    posts = Post.objects.select_related('author').all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj
    }
    if request.headers.get('HX-Request'):
        return render(request, 'baseApp/blog_section.html', {'posts': posts})
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

def create_post(request):
    try:
        if request.method == 'POST':
            form = PostForm(request.POST)
            user = request.user
            if form.is_valid():
                post = form.save(commit=False)
                post.author = user
                post.save()
                messages.success(request, 'Post created successfully!')
                return redirect('home')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = PostForm()
        
        if request.headers.get('HX-Request'):
            return render(request, 'baseApp/create_post.html', {'form': form})
        return render(request, 'baseApp/create_post.html', {'form': form})
    
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('home')

