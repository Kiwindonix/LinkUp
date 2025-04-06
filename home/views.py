from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')  # Шаблон буде в home/templates/home/
