from django import forms


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True)
    reType_password = forms.CharField(widget=forms.PasswordInput, min_length=8, required=True)

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        reType_password = cleaned_data.get('reType_password')

        if new_password and old_password and new_password == old_password:
            self._errors['old_password'] = self.error_class(['New and old Password are the same Enter new Password.'])
            del self.cleaned_data['new_password']
            del self.cleaned_data['reType_password']

        elif new_password and reType_password and new_password != reType_password:
            self._errors['new_password'] = self.error_class(['New Password and reType do not match.'])
            del self.cleaned_data['new_password']
            del self.cleaned_data['reType_password']

        return cleaned_data
