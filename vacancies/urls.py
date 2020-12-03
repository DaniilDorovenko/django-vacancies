from django.urls import path

from vacancies.views import MainView, CompanyView, CompaniesView, \
    VacancyView, VacanciesView, VacancyBySpecialisationView, \
    MyLoginView, MyLogoutView, SignupView, \
    MyCompanyUpdateView, MyCompanyCreateView, \
    MyVacancyUpdateView, MyVacancyView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', VacancyView.as_view(), name='vacancy'),
    path('companies/<int:pk>/', CompanyView.as_view(), name='company'),
    path('companies/', CompaniesView.as_view()),
    path('vacancies/cat/<str:specialisation>/',
         VacancyBySpecialisationView.as_view(), name='vacancy_specialisation'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('mycompany/', MyCompanyUpdateView.as_view(), name='mycompany'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='mycompany_create'),
    path('myvacancies/<int:pk>', MyVacancyUpdateView.as_view(), name='myvacancy_update'),
    path('myvacancy/<int:pk>', MyVacancyView.as_view(), name='myvacancy'),
]
