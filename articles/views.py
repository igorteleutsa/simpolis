from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articles/article_update.html'
    context_object_name = 'article'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    context_object_name = 'article'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


