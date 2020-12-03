from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper


# from vacancies.models import Company, Vacancy

class SignupForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.fields['username'].label = False
        self.fields['first_name'].label = False
        self.fields['last_name'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False


    class Meta:
        model = User
        fields = ("username",
                  "last_name",
                  "first_name")


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.fields['username'].label = False
        self.fields['password'].label = False



# class CompanyEditForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#
#     class Meta:
#         model = Company
#         fields =  ['title',  'employee_count', 'location', 'description', 'logo']
#
#         labels = {
#             'title': 'Название компании',
#             'description': 'Информация о компании',
#             'location': 'География',
#             'employee_count': 'Количество человек в компании',
#             'logo': 'Логотип',
#         }


# class VacancyEditForm(ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#
#     class Meta:
#         model = Vacancy
#         fields =  ['title',  'specialty', 'salary_min', 'salary_max', 'skills', 'description']
#
#         labels = {
#             'title': 'Название вакансии',
#             'specialty': 'Специализация',
#             'salary_min': 'Зарплата от',
#             'salary_max': 'Зарплата до',
#             'skills': 'Требуемые навыки',
#             'description': 'Описание вакансии',
#         }

