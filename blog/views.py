from datetime import timezone
# from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse
from django.utils import timezone


# class SampleTemplateView(TemplateView):
#     template_name = "index.html"

class BlogList(ListView):
    template_name = "post_list.html"
    model = Post
    #paginate_by = 10

class BlogDetail(DetailView):
    model = Post

class BlogCreate(CreateView):

    mode = Post
    fields = ['title', 'text']
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class BlogEdit(UpdateView):
    template_naem = "blog/post_from.html"
    model = Post
    fields = ['title', 'text']

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
 
    def get_form(self):
        form = super(BlogEdit, self).get_form()
        form.fields['title'].label = 'タイトル'
        form.fields['text'].label = 'テキスト'
        # form.author = request.user
        # form.published_date = timezone.now()
        return form

    