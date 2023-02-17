from django import forms
from image_gallery.models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'id': 'custom-file-input'}))

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = ''

    class Meta:
        model = Image
        fields = ['image']
