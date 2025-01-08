from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=200)  # Имя
    bio = models.TextField()  # Описание
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Фото
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # Резюме (PDF или другое)

    def __str__(self):
        return self.full_name

# Места обучения
class Education(models.Model):
    person = models.ForeignKey(on_delete=models.CASCADE, related_name='education_places')
    title = models.CharField(max_length=255)
    graduation_year = models.IntegerField()

# Места работы
class Job(models.Model):
    person = models.ForeignKey(on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    started_at = models.DateField()
    finished_at = models.DateField(null=True, blank=True)

    def save(self):
        # при сохранении модели заменяет день на 1 число(дни не нужно учитывать)
        if self.started_at:
            self.started_at = self.started_at.replace(day=1)

