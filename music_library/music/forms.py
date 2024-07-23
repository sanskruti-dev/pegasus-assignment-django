from django import forms
from .models import Music, Folder

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'genre', 'file']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
