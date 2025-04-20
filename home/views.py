from django.shortcuts import render
from .models import Contact

def home_view(request):
    return render(request, 'home/home.html')  # Шаблон буде в home/templates/home/

def news_view(request):
    return render(request, 'news.html')
def search_contacts(request):

    query = request.GET.get('q')
    results = []
    if query:
        results = Contact.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results})