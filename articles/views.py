import re
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Article, MediaItem


def _render_body(body: str) -> str:
    pattern = re.compile(r'\[([^\|]+)\|(\d+)\]')
    return pattern.sub(
        r'<span class="term-link" data-id="\2" tabindex="0" role="button">\1</span>',
        body
    )


def article_list(request):
    articles = Article.objects.order_by('-created_at')
    return render(request, 'articles/article_list.html',
                  {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    rendered_body = _render_body(article.body)

    sections = []
    for section in article.sections.all():
        sections.append({
            'title': section.title,
            'content': _render_body(section.content),
        })

    from .models import MediaItem
    media_items = MediaItem.objects.all()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'rendered_body': rendered_body,
        'sections': sections,
        'media_items': media_items,
    })


def media_popup(request, media_id):
    try:
        item = get_object_or_404(MediaItem, pk=media_id)

        file_url = ''
        if item.file:
            try:
                # Handle both CloudinaryField and regular FileField
                if hasattr(item.file, 'url'):
                    file_url = item.file.url
                elif hasattr(item.file, 'public_id'):
                    import cloudinary
                    file_url = cloudinary.CloudinaryImage(item.file.public_id).url
                # Force https
                if file_url and file_url.startswith('http://'):
                    file_url = file_url.replace('http://', 'https://', 1)
            except Exception as e:
                file_url = ''

        youtube_id = ''
        if item.youtube_url:
            url = item.youtube_url.strip()
            if 'youtu.be/' in url:
                youtube_id = url.split('youtu.be/')[-1].split('?')[0]
            elif 'v=' in url:
                youtube_id = url.split('v=')[-1].split('&')[0]
            elif 'embed/' in url:
                youtube_id = url.split('embed/')[-1].split('?')[0]

        return JsonResponse({
            'title': item.title,
            'type': item.media_type,
            'text': item.text_content,
            'file_url': file_url,
            'youtube_id': youtube_id,
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)