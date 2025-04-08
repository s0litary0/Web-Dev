from django.contrib import admin
from .models import Company, Vacancy, Position


# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'address')
    search_fields = ['name', 'city', 'address']
    list_filter = ('name',)


admin.site.register(Company, CompanyAdmin)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'salary', 'company')
    # list_display = "__all__"
    search_fields = ['name', 'salary', 'company__name', ]

    list_filter = ('name',)

admin.site.register(Vacancy, VacancyAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Position, PositionAdmin)