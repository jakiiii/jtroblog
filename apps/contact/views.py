from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import CreateView, TemplateView
from django.core.mail import send_mail

from taggit.models import Tag

from base.models import BaseModel
from apps.blog.models import Post
from apps.category.models import Category
from apps.feature.models import SocialMedia, ExtendBlog
from apps.contact.models import ContactInfo

from apps.contact.forms import ContactCreationForm


class ContactView(CreateView):
    form_class = ContactCreationForm
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = "Contact"
        context['feature_post'] = Post.objects.filter(is_feature=True, status=Post.StatusChoices.PUBLISHED).order_by('-created_at')[:5]
        context['category_context'] = Category.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('name')
        context['socialmedia'] = SocialMedia.objects.last()
        context['extend_blog_context'] = ExtendBlog.objects.filter(status=BaseModel.StatusChoices.PUBLISHED).order_by('-created_at')[:10]
        context['tag_context'] = Tag.objects.all().order_by('name')
        context['contact_info'] = ContactInfo.objects.last()
        return context

    def get_success_url(self):
        return reverse('contact:contact')
