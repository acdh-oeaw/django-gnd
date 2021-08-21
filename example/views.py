from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from example.models import MyText, Person

from gnd.forms import GndForm
from . forms import PersonForm


class PersonListView(ListView):
    model = Person
    paginate_by = 10


class PersonCreateView(CreateView):

    model = Person
    form_class = PersonForm
    template_name = 'example/create_person.html'


class PersonDetailView(DetailView):

    model = Person
    template_name = 'example/detail_person.html'


class IndexView(TemplateView):

    template_name = 'example/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GndForm
        return context


class MyTextDetailView(DetailView):

    model = MyText
    template_name = 'example/mytext_detail.html'
