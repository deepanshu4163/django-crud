from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Person

#function based view for index page
def index(request):
    context = {
        'person' : Person.objects.all()
    }
    return render(request, 'myapp/index.html', context)

#class based view for index page
class PersonListView(ListView):
    model = Person
    template_name = 'myapp/index.html'
    context_object_name = 'person'

#detail page
class PersonDetailView(DetailView):
    model = Person

#create page
class PersonCreateView(CreateView):
    model = Person
    fields = ['name', 'date_of_birth', 'address']
    
#update page
class PersonUpdateView(UpdateView):
    model = Person
    fields = ['name', 'date_of_birth', 'address']

#delete confirmation page
class PersonDeleteView(DeleteView):
    model = Person
    success_url = '/myapp'

#function based about page
def about(request):
    return render(request, 'myapp/about.html')