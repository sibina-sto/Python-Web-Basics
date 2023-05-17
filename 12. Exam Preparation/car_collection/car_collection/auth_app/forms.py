from django import forms

from car_collection.auth_app.models import Profile


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
