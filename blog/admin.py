from django.contrib import admin
from .models import Post

# Настрока представление модели Post в административной панели
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug')  # Поля, отображаемые в списке
    list_filter = ('created_at', 'updated_at')  # Фильтрация по дате создания и обновления
    search_fields = ('title', 'content')  # Поля, по которым можно искать
    prepopulated_fields = {'slug': ('title',)}  # Автоматическое заполнение slug из title
    ordering = ('-created_at',)  # Сортировка по дате создания (от новых к старым)
    date_hierarchy = 'created_at'  # Древовидная фильтрация по дате

# Регистрируем модель Post с дополнительной настройкой
admin.site.register(Post, PostAdmin)