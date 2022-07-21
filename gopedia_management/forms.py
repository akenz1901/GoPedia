from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class UserAgentForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'business_name', 'logo')


class UserAgentChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'business_name', 'logo',)
