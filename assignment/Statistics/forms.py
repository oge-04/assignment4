from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)
    manual_input = forms.CharField(widget=forms.Textarea,required=False)
    

