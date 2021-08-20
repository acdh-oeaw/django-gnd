from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from example.models import MyText

from gnd.forms import GndForm


class IndexView(TemplateView):

    template_name = 'example/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GndForm
        return context


class MyTextDetailView(DetailView):

    model = MyText
    template_name = 'example/mytext_detail.html'
