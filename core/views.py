from django.views.generic import TemplateView, FormView
from django.contrib import messages
from core.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o e-mail. Tente novamente.')
        return super(ContactView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'