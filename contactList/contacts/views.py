from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Contact
# Create your views here.


class ContactListView(ListView):
    model = Contact
    template_name = "contact/list.html"


class ContactCreateView(CreateView):
    model = Contact
    fields= ('__all__')
    template_name = "contact/new.html"


class ContactUpdateView(UpdateView):
    model = Contact
    fields= ('__all__')
    template_name = "contact/update.html"


def Contact_detail(request,pk):
    contact = get_object_or_404(Contact,pk=pk)
    context = {
        'contact' : contact
    }
    return render(request,'contact/detail.html',context)



