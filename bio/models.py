from django.db import models


# Личная информация
class Person(models.Model):
    full_name = models.CharField(max_length=200)  # Имя
    about_me = models.TextField()  # Описание
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Фото
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # Резюме (PDF или другое)
    tel = models.CharField(max_length=11, blank=True, null=True)  # Телефон
    email = models.EmailField()  # Почта
    github_url = models.URLField(max_length=500, blank=True, null=True)  # Ссылка на GitHub репозиторий
    another_link_methods = models.TextField()  # Другие способы связи

    def __str__(self):
        return self.full_name


# Места обучения
class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='education_places')
    place = models.CharField(max_length=255)  #Место обучения
    graduation_year = models.IntegerField()  #Год окончания обучения

    class Meta:
        ordering = ('graduation_year',)


# Места работы
class Job(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='jobs')
    place = models.CharField(max_length=255)  # Место работы
    position = models.CharField(max_length=255)  # Должность
    achievements = models.TextField()  # Достижения
    started_at = models.DateField()  # Начало работы(месяц/год, день выставляется первым числом месяца)
    finished_at = models.DateField(null=True, blank=True)  # Конец работы(месяц/год, день выставляется первым числом месяца)

    class Meta:
        ordering = ('started_at',)

    def save(self, *args, **kwargs):
        # при сохранении модели заменяет день на 1 число(дни не нужно учитывать)
        if self.started_at:
            self.started_at = self.started_at.replace(day=1)
        if self.finished_at:
            self.finished_at = self.finished_at.replace(day=1)
        super().save(self, *args, **kwargs)

# Технологии
class Tech(models.Model):
    LEVEL_CHOISES = [('low', 'Начальный'), ('medium', 'Средний'), ('high', 'Высокий')] #варианты уровня
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='techs')
    name = models.CharField(max_length=255)  #Наименование технологии
    level = models.CharField(max_length=6, choices=LEVEL_CHOISES, default='low') #Уровень технологии