from django import forms
from .models import *

class top_tach_form(forms.ModelForm):
    class Meta:
        model=top_tach
        fields='__all__'

class updateform(forms.ModelForm):
    class Meta:
        model=top_tach
        fields='__all__'

class notesFrom(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'

class contact_form(forms.ModelForm):
     class Meta:
        model=contact_us
        fields='__all__'