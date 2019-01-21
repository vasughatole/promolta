from django import forms

from .models import CustomMessage


class MailForm(forms.ModelForm):
    class Meta:
        model = CustomMessage
        fields = ('message_to', 'subject_text', 'message_text')
