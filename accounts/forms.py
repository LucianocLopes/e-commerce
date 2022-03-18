from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserCustom


class UserCustomCreateForm(UserCreationForm):

    class Meta:
        model = UserCustom
        fields = ('first_name', 'last_name', 'phone')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class UserCustomChangeForm(UserChangeForm):

    class Meta:
        model = UserCustom
        fields = ('first_name', 'last_name', 'phone')
