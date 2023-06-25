from django import forms

from GamesPlayApp.models import ProfileModel, GameModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance


class GameBaseForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class GameCreateForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
