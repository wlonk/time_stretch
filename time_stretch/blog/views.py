# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry


class EntryListView(ListView):

    def get_queryset(self):
        return Entry.public.all().order_by('-created')


class EntryDetailView(DetailView):
    model = Entry
    pk_url_kwarg = 'entry_id'

    def get_object(self):
        pk = int(self.kwargs.get(self.pk_url_kwarg, None))
        print pk
        if self.request.user.is_superuser:
            return Entry.private.get(pk=pk)

        elif self.request.user.is_authenticated():
            return Entry.login.get(pk=pk)

        else:
            return Entry.public.get(pk=pk)
