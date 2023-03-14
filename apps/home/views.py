from django.views import View
from django.shortcuts import render


class Home(View):
    # A class based view for the home page
    def get(self, request):
        return render(request, 'index.html')
    