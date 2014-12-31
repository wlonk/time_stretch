# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry
from django.http import HttpResponse


class EntryListView(ListView):

    def get_queryset(self):
        return Entry.public.all().order_by('-created')


class EntryDetailView(DetailView):
    model = Entry
    pk_url_kwarg = 'entry_id'


def entry_test(request):
    return HttpResponse('Hi!')
