from django.contrib import admin

from .models import Vacancy, Company, VacancyApplication


class VacancyAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


class VacancyApplicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(VacancyApplication, VacancyApplicationAdmin)
