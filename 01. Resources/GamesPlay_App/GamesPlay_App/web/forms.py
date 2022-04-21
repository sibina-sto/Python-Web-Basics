from django import forms

from GamesPlay_App.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
        widgets = {
            'email': forms.EmailInput(),
            'age': forms.NumberInput(),
            'password': forms.PasswordInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'profile_picture': forms.URLInput(),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()



class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')
        widgets = {
            'title': forms.TextInput(),
            'rating': forms.NumberInput(),
            'max_level': forms.NumberInput(),
            'image_url': forms.URLInput(),
            'summary': forms.Textarea(),
        }


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')
        widgets = {
            'title': forms.TextInput(),
            'rating': forms.NumberInput(),
            'max_level': forms.NumberInput(),
            'image_url': forms.URLInput(),
            'summary': forms.Textarea(),
        }


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')
        widgets = {
            'title': forms.TextInput(),
            'rating': forms.NumberInput(),
            'max_level': forms.NumberInput(),
            'image_url': forms.URLInput(),
            'summary': forms.Textarea(),
        }
