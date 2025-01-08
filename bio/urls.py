from django.urls import path
from bio.views import personal_page

urlpatterns = [
    path('', personal_page, name='personal_page'),
]