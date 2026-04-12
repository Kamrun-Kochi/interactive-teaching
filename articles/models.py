from django.db import models


class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('youtube', 'YouTube'),
    ]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    text_content = models.TextField(blank=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    youtube_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.media_type})"


class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(
        help_text="Use [word|media_id] to make clickable terms"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    article = models.ForeignKey(
        Article, related_name='sections', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.article.title} — {self.title}"