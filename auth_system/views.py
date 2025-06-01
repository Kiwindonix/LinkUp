from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from auth_system.forms import CustomUserCreationForm


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "auth_system/register.html"
    success_url = reverse_lazy("home")

class UserLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'auth_system/login.html'
    success_url = reverse_lazy('home')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(f"Kористувач {request.user.username} виходить")
        else:
            print("Користувач не аутентифікований, але намагався вийти")
        return super().dispatch(request, *args, **kwargs)
    
class ProfileView(TemplateView):
    template_name = 'portfolio/portfolio.html'

def update_profile(request):
    if request.method == 'POST':
        user = request.user
        if 'profile_image' in request.FILES:
            user.image = request.FILES['profile_image']
            user.save()
        return redirect('profile')  
    return render(request, 'portfolio/portfolio.html', {'user': request.user})