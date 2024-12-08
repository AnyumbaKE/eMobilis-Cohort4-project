from django import forms
from .models import AgentsVerification


class AgentsVerificationForm(forms.ModelForm):

	class Meta:
		model = AgentsVerification
		fields = ('name', 'email', 'phone', 'upload_file',)