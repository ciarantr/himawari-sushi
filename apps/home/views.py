from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ContactForm


class Contact(View):
    # A class based view for the contact page
    def get(self, request):

        form = ContactForm()

        # provide the form with the user's details
        # check if the user is logged in
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            user_full_name = user.get_full_name()
            # pre-populate the form with the user's customer details
            if hasattr(user, 'customer'):
                customer = {
                    'email': user.email,
                    'phone_number': user.customer.phone_number,
                }
                if user_full_name:
                    customer['name'] = user_full_name

                form.initial = customer

        context = {'form': form,
                   'form_title': 'Get in touch',
                   'form_class': 'base-form',
                   'submit_text': 'Send Message',
                   }

        template = 'contact.html'

        return render(request, template, context)

    def post(self, request):
        # TODO: ADD CONTACT CONFIRMATION EMAIL
        form = ContactForm(request.POST)
        if form.is_valid():
            # get the form data
            contact_details = {
                'Name': form.cleaned_data['full_name'],
                'Email': form.cleaned_data['email'],
                'Phone number': form.cleaned_data['phone_number'],
                'Message': form.cleaned_data['message'],
            }

            # format the contact details for the success page
            contact_details = ''.join(
                [f'<div><span>{key}: </span>{value}</div>'
                 for key, value in contact_details.items()])

            messages.success(request, contact_details)
            request.session['contact_form_submitted'] = True

            return redirect('contact_success')

        else:
            context = {'form': form,
                       'form_title': 'Get in touch',
                       'form_class': 'base-form',

                       'submit_text': 'Send Message',
                       }
            return render(request, 'contact.html', context)


class ContactSuccess(View):
    # A class based view for the contact success page
    def get(self, request):
        # check if the contact form was submitted using the session
        # if it was, render the success page
        if request.session.get('contact_form_submitted'):
            del request.session['contact_form_submitted']
            return render(request, 'contact_success.html')
        else:
            return redirect(reverse('contact'))


class Home(View):
    # A class based view for the home page
    def get(self, request):
        return render(request, 'index.html')
    