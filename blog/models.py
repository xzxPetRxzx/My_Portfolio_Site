from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)  # Поле для slug
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Комментарий от {self.author} на пост "{self.post.title}"'
