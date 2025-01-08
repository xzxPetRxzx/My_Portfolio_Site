from django.views.generic import ListView, DetailView
from .models import Portfolio

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'  # Шаблон для отображения списка проектов
    context_object_name = 'projects'  # Переменная, передаваемая в шаблон

    def get_queryset(self):
        return Portfolio.objects.all()  # Выводим все проекты, отсортированные по умолчанию

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'  # Шаблон для отображения деталей проекта
    context_object_name = 'project'  # Переменная, передаваемая в шаблон
