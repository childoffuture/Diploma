from django import forms
from django.forms import ModelForm
from .models import Video, Category


class VideoForm(ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={"style": "width:80%"}))
    id_category = forms.ModelChoiceField(label="Категория", queryset=Category.objects.all(), widget=forms.Select(attrs={"style": "width:80%"}))
    video = forms.FileField(label="")

    class Meta:
        model = Video
        fields = ['name', 'id_category', 'video']

