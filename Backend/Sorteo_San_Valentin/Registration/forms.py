from django.forms import ModelForm,ValidationError
from .models import Registration

class RegistrationForm(ModelForm):

    class Meta:
        model= Registration
        fields = ['email','full_name', 'phone']

    def clean_mail(self):
        email = self.cleaned_data['email'].strip().lower()
        exist = Registration.objects.filter(email__iexact = email).exists()

        if exist:
            raise ValidationError("Este correo ya está registrado")
        return email
    
    def clean_full_name(self):
        name = self.cleaned_data['full_name'].strip()
        return name
    





