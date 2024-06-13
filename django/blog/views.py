from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_list_or_404
from django.views.decorators.http import require_GET
from .models import Article


@require_GET
def home(request):
    p_articles = Article.objects.filter(promoted=True)[:3]
    articles = get_list_or_404(Article)
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page')

    try:
        paginated_articles = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_articles = paginator.page(1)
    except EmptyPage:
        paginated_articles = paginator.page(paginator.num_pages)

    context = {
        'articles': paginated_articles,
        'p_articles': p_articles,
    }
    return render(request, 'home.html', context)


@require_GET
def contact(request):
    return render(request, 'contact.html')
