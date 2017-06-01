from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('email.html')
            context = Context({
                'name': name,
                'email': email,
                'message': message,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Hidden Darkroom" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            messages.add_message(request, messages.SUCCESS, 'Message sent!')
        else:
            messages.add_message(request, messages.ERROR, 'Didn\'t work')

    return render(request, 'contact.html', {
        'form': form_class,
    })
