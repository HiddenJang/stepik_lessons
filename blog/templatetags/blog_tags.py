from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from ..models import Post
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    return Post.published.count()

# Если нужно вызвать с контекстом
# @register.simple_tag(takes_context=True)
# def your_tag(context, your_tag_arg):
#     template_var1 = context.get('template_var1')
#     # ...
#     return val


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).exclude(total_comments=0).order_by('-total_comments')[:count]