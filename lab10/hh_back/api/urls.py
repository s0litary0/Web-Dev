from django.contrib import admin
from django.urls import path

# from .views import companies, company_details, company_vacancies, vacancies, vacancy_details, top_ten_vacancies, \
#     positions, position_details

from .views_module import companies # fbv
from .views_module import CompanyDetailApiView # cbv
from .views_module import CompanyVacanciesListView # generic with mixins
from .views_module import VacanciesList # complex generic

from .views import company_vacancies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', companies),
    path('companies/<int:id>/', CompanyDetailApiView.as_view()),
    path('companies/<int:id>/vacancies', company_vacancies),
    # path('vacancies/', company_vacancies),
    # path('vacancies/<int:id>/', vacancy_details),
    # path('vacancies/top_ten/', top_ten_vacancies),

    # path('positions/', positions),
    # path('positions/<int:id>', position_details),
]
