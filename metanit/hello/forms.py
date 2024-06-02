from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите свое имя", max_length=10)
    age = forms.IntegerField(label="Возраст", help_text="Введите свой возраст", required=False, min_value=1, max_value=120)
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
