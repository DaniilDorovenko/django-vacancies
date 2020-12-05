from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from vacancies.models import VacancyApplication

class SignupForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

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
        self.fields['username'].label = False
        self.fields['password'].label = False


class VacancyApplicationForm(ModelForm):


    class Meta:
        model = VacancyApplication
        fields =  ['written_username',  'written_phone', 'written_cover_letter', ]
