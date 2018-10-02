from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import get_template
# from django.views.generic.base import TemplateView
from django.conf import settings
from post_office import mail
from django.http import HttpResponse, HttpResponseRedirect

# class HomePageView(TemplateView):
#     template_name = 'index.html'
def contact_view(request):
    
    if request.method == "POST":
        name =  request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        #Email ourselves the submitted contact message
        subject = 'Contact Form Received'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.DEFAULT_FROM_EMAIL]

        #Option 1
        # contact_message = "{0}, from {1} with {2}".format(message, name, email)

        # send_mail(subject, contact_message, from_email, to_email, fail_silently=True)  

        #Option 2
        context = {
            'user': name,
            'email': email,
            'message': message
        }

        contact_message =  get_template('contact_message.txt').render(context)

        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        # mail.send(
        #     to_email,
        #     from_email,
        #     template = contact_message,
        #     backend='sendgrid',
        # )

        return render (request, "other.html", {})
    return HttpResponse(render(request, "index.html", {}))

def home(request):
    return HttpResponseRedirect(render(request, "other.html", {}))

  