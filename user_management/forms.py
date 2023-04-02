from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    candidate_nic = forms.CharField(max_length=30, required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.candidate_nic = self.cleaned_data['candidate_nic']
        user.save()
        return user