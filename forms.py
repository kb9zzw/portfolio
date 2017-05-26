from django import forms

class ContactForm(forms.Form):
  first_name = forms.CharField(max_length=100, required=True)
  last_name = forms.CharField(max_length=100, required=True)
  email = forms.EmailField(max_length=100, required=True)
  message = forms.CharField(widget=forms.Textarea(), max_length=1000, required=True)
