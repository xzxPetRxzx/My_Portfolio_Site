from django.urls import path
from . import views

urlpatterns = [
    # Главная страница портфолио
    path('', views.PortfolioListView.as_view(), name='portfolio_list'),  # Главная страница с проектами

    # Детальная страница портфолио (для каждого проекта)
    path('<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),  # Детали проекта
]