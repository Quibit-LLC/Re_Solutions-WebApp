
from django import forms
from .models import *
from django.contrib.auth.models import User
#from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Reset

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter first name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter last name',
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email',
                'class': 'form-control',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Enter password',
                'class': 'form-control',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat password',
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Field('first_name'),
            Field('last_name'),
            Field('email'),
            Field('password1'),
            Field('password2'),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary'),
                Reset('reset', 'Reset', css_class='btn btn-secondary')
            )
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control',
    }))



class ResolutionsForm(forms.ModelForm):
    class Meta:
        model = Resolutions
        exclude = ['created_by', 'updated_at', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categories': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['created_by', 'updated_at', 'created_at']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'license_expiration': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location_description': forms.Textarea(attrs={'class': 'form-control'}),
            'countdown_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EditResolutionForm(forms.ModelForm):
    class Meta:
        model=Resolutions
        INPUT_CLASSES= 'w-full py-4 px-6 rounded-xl border'
        fields=('title','description','notes','priority','due_date','status')
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        exclude = ['created_by', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'url_link': forms.URLInput(attrs={'class': 'form-control'}),
            'categories': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            # Add more fields and widgets as needed
        }