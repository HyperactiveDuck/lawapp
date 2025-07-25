from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, label='Kullanıcı Tipi')
    username = forms.CharField(
        label='Kullanıcı Adı',
        error_messages={
            'required': 'Kullanıcı adı gereklidir.',
        },
        widget=forms.TextInput(attrs={
            'required': False,
            'placeholder': 'Kullanıcı Adı',
            'autocomplete': 'username',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'user_type', 'password1', 'password2')
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta',
            'password1': 'Şifre',
            'password2': 'Şifre (Tekrar)',
        }
        error_messages = {
            'username': {
                'unique': _('Bu kullanıcı adı zaten alınmış.'),
                'required': _('Kullanıcı adı gereklidir.'),
                'invalid': _('Geçersiz kullanıcı adı.'),
            },
            'email': {
                'invalid': _('Geçerli bir e-posta adresi giriniz.'),
                'required': _('E-posta gereklidir.'),
            },
            'user_type': {
                'required': _('Kullanıcı tipi seçilmelidir.'),
                'invalid_choice': _('Geçersiz kullanıcı tipi seçimi.'),
            },
            'password1': {
                'required': _('Şifre gereklidir.'),
                'min_length': _('Şifre çok kısa.'),
            },
            'password2': {
                'required': _('Şifre tekrarı gereklidir.'),
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', _('Şifreler eşleşmiyor.'))
        return cleaned_data

    def add_error(self, field, error):
        if isinstance(error, str):
            error = forms.ValidationError(error)
        super().add_error(field, error)

    def full_clean(self):
        super().full_clean()
        for field in self.errors:
            self.fields[field].error_messages = self.Meta.error_messages.get(field, {})

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Kullanıcı Adı', error_messages={'required': _('Kullanıcı adı gereklidir.')})
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput, error_messages={'required': _('Şifre gereklidir.')})
    error_messages = {
        'invalid_login': _('Geçersiz kullanıcı adı veya şifre.'),
        'inactive': _('Bu hesap aktif değil.'),
    }
