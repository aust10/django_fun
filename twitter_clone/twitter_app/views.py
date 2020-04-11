from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Twitter, Tweet

class TweetListView(ListView):
    model = Twitter
    template_name = 'home_page.html'

class TweetDetailView(DetailView):
    model = Twitter
    template_name = 'twitter_app_detail.html'

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Twitter
    template_name = 'twitter_app_new_twitter.html'
    fields = ['title', 'body_text', 'my_img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Twitter
    template_name = 'twitter_app_delete.html'
    success_url = reverse_lazy('twitter_app:home_page')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class FollowView(View):
    def get(self, request,*args, **kwargs):
        context = {}
        if 'pk' in self.kwargs:
            user = request.user
            newuserobj = User.objects.get(id=self.kwargs['pk'])
            newuserobj.follower.add(user)
            newuserobj.save()
            return redirect(reverse('home_page'))
        context['users'] = User.objects.all().exclude(id=request.user.id)
        return render_to_response('home_page.html.', context, {})