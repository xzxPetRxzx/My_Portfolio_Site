from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonalPageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'bio', 'photo', 'resume')  # Поля, которые будут отображаться в списке
    search_fields = ('full_name', 'bio')  # Поля для поиска
    list_filter = ('full_name',)  # Фильтры в списке объектов
    ordering = ('full_name',)  # Сортировка по умолчанию