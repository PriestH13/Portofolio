from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Projects, Service, About, ContactInfo ,Intro
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.mail import EmailMessage


class HomeView(ListView):
    model = Projects
    template_name = 'port_mat/home.html'
    context_object_name = 'projects'
    queryset = Projects.objects.prefetch_related('images').order_by('-created_at')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all().order_by('created_at')
        context['intro'] = Intro.objects.first()
        return context

class AboutView(TemplateView):
    template_name = 'port_mat/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context

class ProjectsView(ListView):
    model = Projects
    template_name = 'port_mat/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_queryset(self):
        queryset = Projects.objects.prefetch_related('images').order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(technologies__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
class ContactView(TemplateView):
    template_name = 'port_mat/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        context = self.get_context_data()

        if not all([name, email, message]):
            context['error'] = 'Tutti i campi sono obbligatori.'
            return render(request, self.template_name, context)

        if "@" not in email or "." not in email:
            context['error'] = 'Inserisci un indirizzo email valido.'
            return render(request, self.template_name, context)

        try:
            email_message = EmailMessage(
                subject=f'Nuovo messaggio da {name}',
                body=f"Messaggio:\n\n{message}\n\nContatto email: {email}",
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],
            )
            email_message.send(fail_silently=False)

            context['success'] = 'Messaggio inviato con successo!'
            return render(request, self.template_name, context)

        except Exception as e:
            context['error'] = f'Errore nell\'invio del messaggio: {str(e)}'
            return render(request, self.template_name, context)
        
class ServicesView(ListView):
    model = Service
    template_name = 'port_mat/services.html'
    context_object_name = 'services'
    queryset = Service.objects.all().order_by('created_at')