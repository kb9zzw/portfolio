import json

from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import RequestContext
#from django.core.context_processors import csrf
from django.core.mail import mail_admins
from forms import ContactForm

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = """From %s %s <%s>\n\n%s\n""" % (
                form.cleaned_data['first_name'],
                form.cleaned_data['last_name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )

            mail_admins('Contact form', message)

            if request.is_ajax():
                return HttpResponse('OK')
            else:
                pass

        else:
            if request.is_ajax():
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = unicode(e)

                return HttpResponseBadRequest(json.dumps(errors_dict))
            else:
                pass
    else:
        form = ContactForm()

    return render(request, "contact.html", { 'form': form })
