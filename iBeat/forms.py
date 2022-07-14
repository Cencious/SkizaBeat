from django import forms
from iBeat.models import Song 


class UploadMusic(forms.ModelForm):
    Singer_name= forms.CharField(max_length=100, required=False)
    class Meta:
        model = Song
        fields = (
            'title',
            
            'image',
            'song',
            'genre',
        )
            
            
        