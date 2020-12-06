from django.urls import path
from django.contrib.auth.decorators import login_required

from vacancies.views import MainView, CompanyView, CompaniesView, \
    VacancyView, VacanciesView, VacancyBySpecialisationView, \
    MyLoginView, MyLogoutView, SignupView, \
    MyCompanyUpdateView, MyCompanyCreateView, MyCompanyPlugView, \
    MyVacancyUpdateView, MyVacanciesView, MyVacancyCreateView, MyVacancyApplicatiosView,\
    MyResumeUpdateView, MyResumeCreateView, MyResumePlugView, SearchView

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
    path('mycompany/', login_required(MyCompanyUpdateView.as_view()), name='mycompany'),
    path('mycompany/plug/', login_required(MyCompanyPlugView.as_view()), name='mycompany_plug'),
    path('mycompany/create/', login_required(MyCompanyCreateView.as_view()), name='mycompany_create'),
    path('myresume/', login_required(MyResumeUpdateView.as_view()), name='myresume'),
    path('myresume/plug/', login_required(MyResumePlugView.as_view()), name='myresume_plug'),
    path('myresume/create/', login_required(MyResumeCreateView.as_view()), name='myresume_create'),
    path('myvacancy/<int:pk>', login_required(MyVacancyUpdateView.as_view()), name='myvacancy_update'),
    path('myvacancy/create/', login_required(MyVacancyCreateView.as_view()), name='myvacancy_create'),
    path('myvacancies/', login_required(MyVacanciesView.as_view()), name='myvacancies'),
    path('myvacancy/<int:pk>/applications/', login_required(MyVacancyApplicatiosView.as_view()), name='myvacancy_applications'),
    path('search_result/', SearchView.as_view(), name='search_result'),
]
