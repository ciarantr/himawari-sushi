from django.views.generic import TemplateView


class Handler404View(TemplateView):
    # A class based view for the 404 error page

    template_name = 'errors/404.html'

    # send 404 status code
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.status_code = 404
        return response

    # Add meta title, message and status code
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '(404) Whoops! We Can’t Find That Page'
        context['message'] = 'The page your looking for could not be found.'
        context['status_code'] = '404'
        return context


class Handler500View(TemplateView):
    # A class based view for the custom 500 error page

    template_name = 'errors/500.html'

    # send 500 status code
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.status_code = 500
        return response

    # Add meta title, message and status code
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '(500) Whoops! We Messed Up.'
        context['message'] = 'Whoops! We Messed Up.'
        context['status_code'] = '500'
        return context
