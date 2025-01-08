from django.shortcuts import render, get_object_or_404
from .models import Person
from .forms import PersonalPageForm


def personal_page(request):
    # Получаем или создаем объект личной страницы
    personal_page = get_object_or_404(Person, pk=1)  # Можно создать единственную страницу с pk=1

    if request.method == 'POST':
        form = PersonalPageForm(request.POST, request.FILES, instance=personal_page)
        if form.is_valid():
            form.save()
    else:
        form = PersonalPageForm(instance=personal_page)

    return render(request, 'bio/personal_page.html', {'personal_page': personal_page, 'form': form})