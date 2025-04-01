from django.contrib import admin
from .models import Company, Vacancy

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'address')
    search_fields = ['name', 'city', 'address']
    list_filter = ('name',)


admin.site.register(Company, CompanyAdmin)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'salary', 'company')
    search_fields = ['name', 'salary', 'company__name']
    list_filter = ('name',)

admin.site.register(Vacancy, VacancyAdmin)
