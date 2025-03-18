from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CtiLog
from .models import BlackListIP
from .models import BlackListURL

class CtiLogForm(forms.ModelForm):
    class Meta:
        model = CtiLog
        fields = ['cve', 'signature', 'description', 'response_measures']


class BlackListIp(forms.ModelForm):
    class Meta:
        model = BlackListIP
        fields = ['ip_source', 'attack_date',  'country_source']

class BlackListURL(forms.ModelForm):
    class Meta:
        model = BlackListURL
        fields = ['url_source', 'attack_date']


class CtiLogSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        label="Поиск по CVE или сигнатуре",
        widget=forms.TextInput(attrs={'placeholder': 'Введите CVE или сигнатуру'})
    )

    def clean_search_query(self):
        # Очистим строку поиска, удалив пробелы
        search_query = self.cleaned_data.get('search_query')
        if search_query:
            search_query = search_query.replace(' ', '').lower()
        return search_query

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))