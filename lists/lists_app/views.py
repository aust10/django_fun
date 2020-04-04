from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import ListItem



def index(request):
    context = {
        'latest_lists_items':ListItem.objects.filter(is_comp=False).order_by('pub_date'),
        'finnished_lists_items':ListItem.objects.filter(is_comp=True).order_by('comp_date')
    }
    return render(request, "lists_app/index.html", context)

def add_it(request):
    entry = request.POST['list_entry']
    ListItem.objects.create(items=entry, pub_date=timezone.now())
    return HttpResponseRedirect(reverse('lists_app:index'))

def to_compleated(request, completed_id):
    completed = get_object_or_404(ListItem, pk=completed_id)
    completed.is_comp = True
    completed.comp_date = timezone.now()
    completed.save()

    return HttpResponseRedirect(reverse('lists_app:index'))

def delete_it(request):
    delete_item = ListItem.objects.filter(is_comp=True)

    for items in delete_item:
        items.delete()
    return HttpResponseRedirect(reverse('lists_app:index'))


