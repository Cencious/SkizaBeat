from django import forms
from .models import Song

class UploadMusic(forms.ModelForm):
    singer= forms.CharField(max_length=100, required=False)
    class Meta:
        model = Song
        fields = (
            'title',
            'image',
            'song',
            'genre',
        )