from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import Contact, Resolutions
# Create your views here.

@csrf_protect  
def signup(request):
    # Ensuring that the form is saved
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form
    })


def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def index(request):
    # Assuming you have a view function that retrieves the contact details
    contact_info = Contact.objects.last()  # You might want to retrieve based on some criteria
    return render(request, 'index.html', {'contact_info': contact_info})

@login_required
def create_resolution(request):
    if request.method == 'POST':
        form = ResolutionsForm(request.POST)
        if form.is_valid():
            # You might want to set the user who created the resolution here
            form.instance.created_by = request.user
            form.save()
            return redirect('resolutions')  # Redirect to a success page or another view
    else:
        form = ResolutionsForm()

    return render(request, 'create_resolution.html', {'form': form})

@login_required
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # You might want to set the user who created the contact here
            form.instance.created_by = request.user
            form.save()
            return redirect('index')  # Redirect to a success page or another view
    else:
        form = ContactForm()

    return render(request, 'create_contact.html', {'form': form})

def resolution(request):
    # Filter resolutions based on the current user
    resolutions = Resolutions.objects.filter(created_by=request.user)
    return render(request, 'resolutions.html', {'resolutions': resolutions})

@login_required
def delete_resolution(request, pk):
    patient = get_object_or_404(Resolutions, pk=pk, created_by=request.user)
    patient.delete()

    return redirect('resolutions')

@login_required   
def edit_resolution(request, pk):
    resolution = get_object_or_404(Resolutions, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditResolutionForm(request.POST, request.FILES, instance=resolution)
        if form.is_valid():
            form.save()
            return redirect('resolutions')  # Use 'patient_id' instead of 'pk'
    else:
        form = EditResolutionForm(instance=resolution)
    return render(request, 'create_resolution.html', {
        'form': form,
    })

@login_required
def create_news_article(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            news_article = form.save(commit=False)
            news_article.created_by = request.user
            news_article.save()
            return redirect('news_article_detail', pk=news_article.pk)
    else:
        form = NewsArticleForm()

    return render(request, 'create_news_article.html', {'form': form})

def all_news_articles(request):
    news_articles = NewsArticle.objects.all().order_by('-created_at')
    return render(request, 'all_news_articles.html', {'news_articles': news_articles})

@login_required
def news_article_detail(request, pk):
    news_article = NewsArticle.objects.get(pk=pk)
    return render(request, 'news_article_detail.html', {'news_article': news_article})