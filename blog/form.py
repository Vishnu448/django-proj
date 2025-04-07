from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField( required=True)
    message=forms.CharField(widget=forms.Textarea)
    
class RegisterForm(forms.ModelForm):
    username=forms.CharField(label='Username',max_length=100,required=True)
    email=forms.CharField(label='email',max_length=100,required=True)
    password=forms.CharField(label='password',max_length=100,required=True)
    confirm_password=forms.CharField(label='confirm password',max_length=100,required=True)
    
    class Meta:
        model=User
        fields=['username','email','password','confirm_password']