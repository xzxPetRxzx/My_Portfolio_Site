from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'technologies', 'completed_on', 'github_url', 'website_url', 'slug')
    prepopulated_fields = {'slug': ('title',)}  # Автоматически генерируем slug из названия проекта
    search_fields = ('title', 'technologies', 'description')  # Добавляем поиск по полям
    list_filter = ('completed_on', 'technologies')  # Добавляем фильтры по дате и технологиям