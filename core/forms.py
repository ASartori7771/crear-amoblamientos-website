from django import forms 

class ContactForm(forms.Form):
    from_name = forms.CharField(max_length=100)
    reply_to = forms.EmailField()
    title = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)
