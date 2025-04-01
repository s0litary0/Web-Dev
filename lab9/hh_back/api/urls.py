from django.contrib import admin
from django.urls import path

from .views import companies, company_details, company_vacancies, vacancies, vacancy_details, top_ten_vacancies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', companies),
    path('companies/<int:id>/', company_details),
    path('companies/<int:id>/vacancies', company_vacancies),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy_details),
    path('vacancies/top_ten/', top_ten_vacancies)

]
