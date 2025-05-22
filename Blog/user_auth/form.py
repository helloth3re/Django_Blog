from django import forms
from django.contrib.auth import authenticate


class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request  # Django passes this automatically
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(self.request, username=email, password=password)

        if not user:
            raise forms.ValidationError("Invalid email or password.")

        self.user = user
        return self.cleaned_data

    def get_user(self):
        return self.user
