from django.contrib.auth import forms as auth_forms
from blog_system.common import form_mixins


class SignUpForm(form_mixins.BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()


class SignInForm(form_mixins.BootstrapFormMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()
