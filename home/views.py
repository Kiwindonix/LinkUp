from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Post, Like, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.db import models

def news_view(request):
    return render(request, 'news.html')

def search_contacts(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Contact.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results})

def home(request):
    sort_by = request.GET.get('sort', 'date')  # значення за замовчуванням

    if sort_by == 'likes':
        posts = Post.objects.all().annotate(like_count=models.Count('likes')).order_by('-like_count', '-created_at')
    elif sort_by == 'comments':
        posts = Post.objects.all().annotate(comment_count=models.Count('comments')).order_by('-comment_count', '-created_at')
    else:  # сортування за датою
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home/home.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Якщо вже лайкнув, видаляємо
    return redirect('home')

@login_required
def comment_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        text = request.POST.get('comment')
        if text:
            Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('home')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'home/create_post.html', {'form': form})