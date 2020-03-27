
from django import forms

from cinema_app.accounts.models import Customer

from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    birthdate = forms.DateField(input_formats=['%Y/%m/%d','%m/%d/%Y','%m/%d/%y'])

    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name')

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Passwords don't match"
            raise forms.ValidationError(msg)
        return password2

    def clean_email(self):

        email = self.cleaned_data.get('email')

        try:
            Customer.objects.filter(email=email)
        except Customer.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.birthdate = self.cleaned_data["birthdate"]

        username = user.last_name
        counter = 1
        while Customer.objects.filter(username=username):
            username = user.last_name + '_' + str(counter)
            counter += 1
        user.username = username

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Customer
        fields = ()

    def clean_password(self):
        # always return the initial value
        return self.initial['password']