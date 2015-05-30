from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='Name',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, label='Repeat password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='Name',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class NewTask(forms.Form):
    script = forms.FileField(required=True, label='Script')
    csv_data = forms.FileField(required=True, label='CSV Data')
