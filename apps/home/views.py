from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.utils.safestring import mark_safe
from django.views import View

from .forms import ContactForm, SubscribeForm


# Create your views here.
class About(View):
    # A class based view for the about page
    def get(self, request):
        return render(request, 'about.html')


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

            # send contact details to contact success page
            request.session['contact_details'] = contact_details

            messages.success(request, 'Success! Your message has been sent.')
            return redirect(reverse('contact_success'))
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
        # check if the contact details are in the session
        # if they are, display them on the success page
        if request.session.get('contact_details'):
            contact_details = request.session['contact_details']
            # remove the contact details from the session
            del request.session['contact_details']
            context = {'contact_details': mark_safe(contact_details)}
            return render(request, 'contact_success.html', context)
        else:
            return redirect(reverse('contact'))


class Home(View):
    # A class based view for the home page
    def get(self, request):
        form = SubscribeForm()
        context = {'form': form}

        return render(request, 'index.html', context)

    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            # format the contact details for the success page
            email_details = {
                'Email': form.cleaned_data['email'],
            }

            email_details = ''.join(
                [f'<div><span>{key}: </span>{value}</div>'
                 for key, value in email_details.items()])

            # send email details to subscribe success page
            request.session['email_details'] = email_details

            messages.success(
                request, f'Success! We will send you your discount soon.'
            )
            return redirect(reverse('subscribe_success'))
        else:
            context = {'form': form}
            messages.error(
                request,
                'Error! Looks like there\'s a problem with your email.'
            )
            return render(request, 'index.html', context)


class Menu(View):
    # A class based view for the menu page
    def get(self, request):
        # list of available menu items
        raw_roll = [
            ('Tuna Roll', 5.95),
            ('Salmon- Roll', "5.95"),
            ('Alaska Roll Salmon', "5.95"),
            ('Yellowtall- Scallion', "5.95"),
            ('Tuna Avocado', "7.95"),
            ('Tuna Cucumber', "7.95"),
            ('Yellowtall Jalapeño', "4.35"),
            ('Salmon Avocado', "7.95"),
            ('Salmon Cucumber', "7.95"),
            ('Spicy Tuna', "7.95"),
            ('Spicy Salmons', "8.00"),
            ('Spicy Yellowtail', '8.95')
        ]

        cooked_roll = [
            ("Eel Avocado", "7.00"),
            ("Eel Cucumber", "7.00"),
            ("Philadelphia", "7.00"),
            ("Spicy Snow Crab", "7.00"),
            ("Sweet Potato Tempura", "6.00"),
            ("Crabmeat Cheese", "6.50"),
            ("Avocado", "5.00"),
            ("Cucumber", "5.00"),
            ("Peanut Avocado", "6.00"),
            ("California", "7.00"),
            ("Cucumber Avocado", "5.00"),
            ("Shrimp Tempura", "7.00")
        ]

        menu = {
            'raw_roll': raw_roll,
            'cooked_roll': cooked_roll,
        }

        context = {'menu': menu}
        template = 'menu.html'

        return render(request, template, context)


class Reservations(View):
    # A class based view for the reservation page
    def get(self, request):
        # list of questions and answers reservation page
        questions = [
            {
                'question': 'How do I make a reservation?',
                'answer': 'You can make a reservation by calling'
                          ' us at 555-555-5555 or by making a ',
                'link': 'booking_create',

            },
            {
                'question': 'How do I cancel a reservation?',
                'answer': 'You can cancel a reservation by calling us at'
                          '555-555-5555 or by making '
                          'a change on your profile page in the booking '
                          'option.'

            },
            {
                'question': 'What if I have a food allergy?',
                'answer': 'Please let us know about your food allergy when you'
                          'make your reservation. We will do our best to '
                          'accommodate your needs.',
            }

        ]
        context = {'questions': questions}
        template = 'reservations.html'

        return render(request, template, context)


class SubscribeSuccess(View):
    # A class based view for the subscribe success page
    def get(self, request):
        # check if the email details are in the session
        # if they are, display them on the success page
        if request.session.get('email_details'):
            email_details = request.session['email_details']
            # remove the email details from the session
            del request.session['email_details']
            context = {'email_details': mark_safe(email_details)}
            return render(request, 'subscribe_success.html', context)
        else:
            return redirect(reverse('home'))
