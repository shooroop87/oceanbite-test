from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
import logging
from .forms import ContactForm

log = logging.getLogger(__name__)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Static popular species (placeholder content)
        ctx['popular_species'] = [
            {'name': 'Лосось атлантический', 'desc': 'Филе, порции, копчёный', 'img': 'img/placeholders/photo-1x1.jpg'},
            {'name': 'Форель', 'desc': 'Филе, порции', 'img': 'img/placeholders/photo-1x1.jpg'},
            {'name': 'Икра', 'desc': 'Крупная, премиум', 'img': 'img/placeholders/photo-1x1.jpg'},
        ]
        return ctx

class AboutView(TemplateView):
    template_name = 'about.html'

class SpeciesView(TemplateView):
    template_name = 'species.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['species'] = [
            {{'name': 'Лосось Whole', 'desc': 'Дикая выловка, EU', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Лосось Филе', 'desc': 'Скин-он/скин-офф', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Лосось Порции', 'desc': 'Инд. вакуум', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Копчёный лосось', 'desc': 'Натуральное копчение', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Солёный лосось', 'desc': 'Гравлакс', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Форель', 'desc': 'Филе, порции', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Икра', 'desc': 'Выбор позиций', 'img': 'img/placeholders/photo-16x9.jpg'}},
            {{'name': 'Скумбрия', 'desc': 'Ассортимент', 'img': 'img/placeholders/photo-16x9.jpg'}},
        ]
        return ctx

class GalleryView(TemplateView):
    template_name = 'gallery.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['images'] = ['img/placeholders/photo-16x9.jpg'] * 12
        return ctx

class ContactView(FormView):
    template_name = 'contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):
        data = form.cleaned_data
        log.info('Contact form: %s', data)  # emulate email send
        messages.success(self.request, 'Спасибо! Мы получили ваше сообщение и скоро свяжемся.')
        return super().form_valid(form)

def custom_404(request, exception):
    return TemplateView.as_view(template_name='404.html')(request, status=404)

def custom_500(request):
    return TemplateView.as_view(template_name='500.html')(request, status=500)
