from django.urls import path

from vacancies.views import MainView, CompanyView, CompaniesView, \
    VacancyView, VacanciesView, VacancyBySpecialisationView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('companies/<int:pk>/', CompanyView.as_view(), name='company'),
    path('companies/', CompaniesView.as_view()),
    path('vacancies/cat/<str:specialisation>/',
         VacancyBySpecialisationView.as_view(), name='vacancy_specialisation'),
]
