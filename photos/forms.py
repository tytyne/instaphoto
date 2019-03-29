from django import forms
from .models import Image,Profile.

class PhotosLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
class PhotoImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date', 'tags']
class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']        