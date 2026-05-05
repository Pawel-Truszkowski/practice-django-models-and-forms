from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from .models import Article, Category


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Received contact form submission: Email: {email}, Message: {message}")
            return render(request, 'blog/contact.html', context={'form': ContactForm(), 'success': True})
        else:
            return render(request, 'blog/contact.html', context={'form': form, 'success': False})
    else:
        form = ContactForm()
        return render(request, 'blog/contact.html', context={'form': form})


def recent_django_articles(request):
    recent_articles = Article.objects.filter(title__icontains='django').all()
    articles_order_by_date = Article.objects.filter(published_at__gte='2024-01-01').all()
    data = {
        'recent_articles': list(recent_articles.values()),
        'articles_order_by_date': list(articles_order_by_date.values())
    }
    return JsonResponse(data, json_dumps_params={'indent': 4})