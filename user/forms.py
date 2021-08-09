from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Passward"}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password",
                               forms.ValidationError("비밀번호가 틀렸습니다."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("존재하지 않는 사용자입니다."))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("nickname", "email")
        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "nickname"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm Password"}))
    field_order = [
        "nickname",
        "email",
        "password",
        "password1",
    ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            models.User.objects.get(username=email)
            raise forms.ValidationError("이미 존제하는 이메일입니다.")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data["password1"]
        if password != password1:
            raise forms.ValidationError("확인 비밀번호가 같지 않습니다.")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        nickname = self.cleaned_data.get("nickname")
        user.nickname = nickname
        user.username = email
        user.set_password(password)
        user.save()
