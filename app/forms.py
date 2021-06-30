from django import forms
from .models import Expert

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')



class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = "__all__"