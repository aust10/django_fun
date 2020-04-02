from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import ListItem



class IndexView(generic.ListView):
    template_name= 'lists_app/index.html'
    context_object_name ='latest_lists_items'

    def get_queryset(self):
        return ListItem.objects.filter(comp_date=timezone.now())
         
     
     
def add_it(request):
    entry = request.POST['list_entry']
    ListItem.create(items=entry, pub_date=timezone.now())
    return HttpResponseRedirect(reverse('list_app:index'))

def to_compleated(request):
    completed = get_object_or_404(ListItme, pk=completed_id)
    completed.is_comp = True
    completed.comp_date = timezone.now()
    completed.save()

    return HttpResponseRedirect

def delete_it(request):
    delete_item = ListItem.objects.filter(is_comp=True)

    for items in delete_item:
        items.delete()
    return HttpResponseRedirect(reverse('list_app:index'))


