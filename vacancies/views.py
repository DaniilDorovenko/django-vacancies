from django.db.models import Count, Q
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from vacancies.forms import SignupForm, LoginForm, VacancyApplicationForm
from vacancies.models import Vacancy, Company, Specialty, VacancyApplication, Resume


class MainView(View):

    def get(self, request):

        specialisations = Specialty.objects\
            .values('title', 'code')\
            .annotate(vacancy_count=Count('vacancy'))
        companies = Company.objects\
            .values('title', 'logo', 'id',)\
            .annotate(vacancy_count=Count('vacancy'))

        return render(request, 'index.html', {
            'specialisations': specialisations,
            'companies': companies})


class VacanciesView(ListView):
    model = Vacancy


class VacancyView(DetailView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyView, self).get_context_data(**kwargs)
        context['form'] = VacancyApplicationForm
        return context

    def post(self, request, pk):
        form = VacancyApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                application = VacancyApplication.objects.create(
                    written_username=data['written_username'],
                    written_phone=data['written_phone'],
                    written_cover_letter=data['written_cover_letter'],
                    vacancy=Vacancy.objects.get(id=pk),
                    applicant=request.user)
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in e.args[0]:
                    print('Вы уже оставили отклик')

        elif 'written_phone' not in form.cleaned_data:
            print('Неверный формат номера')
            form.add_error('written_phone','Неверный формат номера, используйте "+X XXX XXX XX XX"')

        return redirect('vacancy', pk=pk)


class VacancyBySpecialisationView(View):

    def get(self, request, specialisation):
        vacancy = Vacancy.objects.filter(specialty__code=specialisation)
        specialisation = Specialty.objects.get(code=specialisation).title
        return render(request, 'vacancies/vacancy_list.html',
                      {'object_list': vacancy,
                       'specialisation': specialisation})


class CompanyView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            company_id=context['object'].id)
        return context


class MyCompanyPlugView(View):

    def get(self, request):
        return render(request, 'company_plug.html')


class CompaniesView(ListView):
    model = Company


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    authentication_form = LoginForm


class MyLogoutView(LogoutView):
     pass


class SignupView(CreateView):
     form_class = SignupForm
     success_url = '/login'
     template_name = 'register.html'


class MyCompanyUpdateView(SuccessMessageMixin, UpdateView):
    model = Company
    fields = ['title',  'employee_count', 'location', 'description', 'logo']
    success_message = 'Компания обновлена'
    success_url = '/mycompany/'

    def dispatch(self, request, *args, **kwargs):
        try:
            mycompany = Company.objects.get(owner = self.request.user)
        except Company.DoesNotExist:
            return redirect('mycompany_plug')
        self.get_object()

        return super(MyCompanyUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        mycompany = Company.objects.get(owner=self.request.user)
        return mycompany


class MyCompanyCreateView(SuccessMessageMixin, CreateView):
    model = Company
    fields = ['title',  'employee_count', 'location', 'description', 'logo', ]
    success_message = 'Компания создана'
    success_url = '/mycompany/'

    def form_valid(self, form):
        company = form.save(commit=False)
        company.owner = self.request.user
        company.save()
        return redirect('mycompany')


class MyVacanciesView(View):

    def get(self, request):
        myvacancies = Vacancy.objects.filter(company__owner=request.user)\
            .annotate(appication_count=Count('vacancyapplication'))
        return render(request, 'my-vacancy-list.html',{'myvacancies': myvacancies})


class MyVacancyUpdateView(SuccessMessageMixin, UpdateView):
    model = Vacancy
    fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
    success_message = 'Вакансия обновлена'
    success_url = '/myvacancies/'

    def get_context_data(self, **kwargs):
        context = super(MyVacancyUpdateView, self).get_context_data(**kwargs)
        context['applications'] = VacancyApplication.objects.filter(vacancy__id=self.kwargs['pk'])
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            mycacancy = Company.objects.get(vacancy__id=self.kwargs['pk'], owner=self.request.user)
        except Company.DoesNotExist:
            return redirect('myvacancies')
        return super(MyVacancyUpdateView, self).dispatch(request, *args, **kwargs)


class MyVacancyCreateView(CreateView):
    model = Vacancy
    fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']

    def form_valid(self, form):
        vacancy = form.save(commit=False)
        vacancy.company = Company.objects.get(owner=self.request.user)
        vacancy.save()
        messages.success(self.request, 'Вакансия добавлена')
        return redirect('myvacancies')

class MyVacancyApplicatiosView(ListView):
    model = VacancyApplication

    def get_queryset(self, **kwargs):
        applications = VacancyApplication.objects.filter(vacancy_id=self.kwargs['pk'])
        return applications


class MyResumePlugView(View):

    def get(self, request):
        return render(request, 'resume_plug.html')


class MyResumeUpdateView(SuccessMessageMixin, UpdateView):
    model = Resume
    fields = ['status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
    success_message = 'Резюме обновлено'
    success_url = '/myresume/'

    def dispatch(self, request, *args, **kwargs):
        try:
            myresume = Resume.objects.get(owner = self.request.user)
        except Resume.DoesNotExist:
            return redirect('myresume_plug')
        self.get_object()

        return super(MyResumeUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        myresume = Resume.objects.get(owner=self.request.user)
        return myresume


class MyResumeCreateView(SuccessMessageMixin, CreateView):
    model = Resume
    fields = ['status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
    success_message = 'Резюме создано'
    success_url = '/myresume/'

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.owner = self.request.user
        resume.save()
        return redirect('myresume')

class SearchView(View):

    def get(self, request):
        query = self.request.GET.get('query')
        vacancy = Vacancy.objects.filter(
            Q(company__vacancy__title__icontains=query) |
            Q(company__vacancy__description__icontains=query)
            | Q(company__vacancy__skills__icontains=query))
        return render(request, 'search_results.html',  {'vacancies': vacancy})


def page_not_found(request, exception):
    return HttpResponse('Нету такой страницы!')


def server_error(exception):
    return HttpResponse('Что-то сломалось, но мы обязательно починим!')
