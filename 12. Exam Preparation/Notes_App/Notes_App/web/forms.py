from django import forms

from Notes_App.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        self.instance.delete()
        Note.objects.all().delete()
        return self.instance


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
