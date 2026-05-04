from django.shortcuts import render
from .forms import ContactForm


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