from django.http import HttpResponse
from blog.models import Post, Comment
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse


def index(request, selected_page=1):
    #Grab all the posts
    posts = Post.objects.order_by("-pub_date")

    #Take the ones from the selected page
    pages = Paginator(posts, 5)

    #Get the specified page or, if specified page is empty, the last page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    context = {'posts': returned_page.object_list, 'page': returned_page}
    return render(request, 'blog/index.html', context)


def category(request, category_slug, selected_page=1):
    #Grab all the posts
    category_posts = Post.objects.all().filter(categories__slug__exact=category_slug).order_by("-pub_date")

    #Take the ones from the selected page
    pages = Paginator(category_posts, 5)

    #Get the specified page or, if specified page is empty, the last page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    context = {'posts': returned_page.object_list, 'page': returned_page, 'category_slug': category_slug}
    return render(request, 'blog/category.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

# To do: def get_category(request, categorySlug, selected_page=1):


class Rss(Feed):
    title = "Jack Carter's Blog"
    link = "rss/"
    description = "Posts by Jack Carter"

    def items(self):
        return Post.objects.all().order_by("-pub_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return reverse('blog:post_detail', args=[item.slug,])