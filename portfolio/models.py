from django.db import models
from django.utils.text import slugify

class Portfolio(models.Model):
    title = models.CharField(max_length=200)  # Название проекта
    description = models.TextField()  # Полное описание проекта
    short_description = models.CharField(max_length=300, blank=True)  # Краткое описание
    technologies = models.CharField(max_length=500, blank=True)  # Технологии, использованные в проекте
    completed_on = models.DateField(null=True, blank=True)  # Дата завершения проекта
    github_url = models.URLField(max_length=500, blank=True, null=True)  # Ссылка на GitHub репозиторий
    website_url = models.URLField(max_length=500, blank=True, null=True)  # Ссылка на сайт проекта
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)  # Изображение проекта
    video_url = models.URLField(max_length=500, blank=True, null=True)  # Ссылка на видео (например, демо)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Slug для создания красивых URL

    def save(self, *args, **kwargs):
        # Автоматическая генерация slug, если его нет
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title