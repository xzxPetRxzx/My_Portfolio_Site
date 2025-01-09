from django.contrib import admin
from .models import Person, Education, Job, Tech


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'about_me', 'photo', 'resume', 'tel','email', 'github_url', 'another_link_methods')  # Поля, которые будут отображаться в списке
    search_fields = ('full_name', 'about_me')  # Поля для поиска
    list_filter = ('full_name',)  # Фильтры в списке объектов
    ordering = ('full_name',)  # Сортировка по умолчанию

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('person', 'place', 'graduation_year')
    search_fields = ('place','graduation_year')
    list_filter = ('person',)
    ordering = ('person',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('person', 'place', 'position', 'achievements', 'started_at', 'finished_at')
    ordering = ('person',)

@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', 'level')
    ordering = ('person',)