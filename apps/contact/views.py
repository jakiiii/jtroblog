from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from apps.contact.forms import EmailPostForm

from apps.blog.models import Post


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = "Contact"
        return context


def post_share(request, post_id):
    template_name = 'contact/post/share.html'
    post = get_object_or_404(Post, id=post_id, status=Post.StatusChoices.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    context = {
        'post': post,
        'form': form
    }
    return render(request, template_name, context)
