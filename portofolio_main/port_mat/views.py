from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Projects
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

class HomeView(ListView):
    model = Projects
    template_name = 'port_mat/home.html'
    context_object_name = 'projects'
    queryset = Projects.objects.prefetch_related('images').order_by('-created_at')[:3]

class AboutView(TemplateView):
    template_name = 'port_mat/about.html'

class ProjectsView(ListView):
    model = Projects
    template_name = 'port_mat/projects.html'
    context_object_name = 'projects'
    queryset = Projects.objects.prefetch_related('images').order_by('-created_at')

class ContactView(TemplateView):
    template_name = 'port_mat/contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        
        if not all([name, email, message]):
            return render(request, self.template_name, {
                'error': 'Tutti i campi sono obbligatori.'
            })

        try:
            send_mail(
                subject=f'Messaggio da {name}',
                message=message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER], 
                fail_silently=False,
            )
            return render(request, self.template_name, {
                'message': 'Messaggio inviato con successo!'
            })
        except Exception as e:
            return render(request, self.template_name, {
                'error': f'Errore nell\'invio del messaggio: {str(e)}'
            })
