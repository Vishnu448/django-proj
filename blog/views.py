from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Post,About
from django.core.paginator import Paginator
from .form import ContactForm,RegisterForm
import logging
from rest_framework import status
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework import status, views
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password




def index(request):
    all_posts = Post.objects.all().order_by('-created_at')  # Ensure ordering
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blogs/index.html', {"page_obj": page_obj})

def detail(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    return render(request, 'blogs/detail.html', {"post": post, "related_posts": related_posts})

def old_url_redirect(request):
    return redirect((reverse("blog:new_url")))

def new_url_redirect(request):
    return HttpResponse("This is a new URL")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger("Testing")
        
        if form.is_valid():
            logger.debug(f"Form data is {form.cleaned_data['name']}, {form.cleaned_data['email']}, {form.cleaned_data['message']}")
            # Change success_message to success to match your template
            return render(request, 'blogs/contact.html', {
                'form': form,
                'success': "Form submitted successfully"  # Changed key to match template
            })
        else:
            logger.debug("Form data is invalid")
            return render(request, 'blogs/contact.html', {
                'form': form,
                'name': name,
                'email': email,
                'message': message
            })
    else:
        form = ContactForm()
    
    return render(request, 'blogs/contact.html', {'form': form})

def about_view(request): 
    about, created = About.objects.get_or_create(
        defaults={'content': 'No Contents'}
    )
    return render(request, 'blogs/about.html', {"about": about})

# accounts/views.py

def register_page(request):
    """
    Render the registration page
    """
    return render(request, 'blogs/register.html')


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # First, get the user by username
            user = User.objects.get(username=username)  # Note: username not User_name
            
            # Check if the password matches using Django's check_password function
            if check_password(password, user.password):
                # Store user info in session to maintain login state
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                
                # Redirect to index page on successful login
                return redirect('index')
            else:
                # Password doesn't match
                messages.error(request, 'Invalid username or password')
        except User.DoesNotExist:
            # User doesn't exist
            messages.error(request, 'Invalid username or password')
            
    # For both GET requests and failed logins
    return render(request, 'blogs/login.html')
            
    
    # For GET requests, just show the login form
   



 







    
    
