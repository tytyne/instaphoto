from django import forms
from .models import Image

class PhotosLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
class PhotoImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['editor', 'pub_date', 'tags']