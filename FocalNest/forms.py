# forms.py
from django import forms
from .models import Enquiry, ServicePost

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'interested_in', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'interested_in': forms.Select(),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the interested_in field queryset for your specific case
        self.fields['interested_in'].queryset = ServicePost.objects.all()
        
        choices = [(None, "I'm interested in")]
        choices += [(service.id, str(service)) for service in self.fields['interested_in'].queryset]
        self.fields['interested_in'].choices = choices
