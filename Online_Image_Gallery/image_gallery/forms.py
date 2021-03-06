from django import forms
from image_gallery.models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ['image']
