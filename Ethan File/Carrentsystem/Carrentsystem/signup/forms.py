from django import forms

class CustomerSignInForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class StaffSignInForm(forms.Form):
    staff_number = forms.IntegerField(widget=forms.TextInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class CustomerSignUpForm(forms.Form):
    GENDER =(
        ('male', 'male'),
        ('female', 'female'),
    )
    first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, widget=forms.TextInput())
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    email_address = forms.EmailField(widget=forms.EmailInput())
    gender = forms.ChoiceField(choices=GENDER)
