from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=120, widget=forms.TextInput(attrs={
        'placeholder': 'Ваше имя', 'class': 'form-input'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'name@example.com', 'class': 'form-input'
    }))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={
        'rows': 6, 'placeholder': 'Ваш запрос', 'class': 'form-textarea'
    }))

    def clean_message(self):
        data = self.cleaned_data['message']
        if len(data.strip()) < 10:
            raise forms.ValidationError('Пожалуйста, напишите сообщение подробнее (от 10 символов).')
        return data
