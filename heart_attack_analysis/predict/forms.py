from dataclasses import fields
from email.policy import default
from django import forms
from matplotlib import widgets
from matplotlib.pyplot import title
from .models import Prediction

class NewForm(forms.ModelForm):
    class Meta:
        CHOICES= (
            ('1','В норме'),
            ('2','Выше нормы'),
            ('3','Значительно выше нормы'),
            )
        GENDERS = (
            ('1','Ж'),
            ('2','М'),
        )
        model = Prediction
        fields = '__all__'
        widgets = {
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}, choices=GENDERS),
            'height': forms.NumberInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'ap_hi': forms.NumberInput(attrs={'class':'form-control'}),
            'ap_lo': forms.NumberInput(attrs={'class':'form-control'}),
            'cholesterol': forms.Select(attrs={'class':'form-control'}, choices=CHOICES),
            'gluc': forms.Select(attrs={'class':'form-control'}, choices=CHOICES),
            'years': forms.NumberInput(attrs={'class':'form-control'})
        }

