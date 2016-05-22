from django import forms

from amer.models import Character


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required = False, label='e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
    
class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['power','speed']

    '''
    clean_fieldName
    '''
    def clean_speed(self):
        data = self.cleaned_data['power']
        print (self.cleaned_data)
        return data
    

 
class menuForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
   
