from django import forms
from models import UserProfile, Status

class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile
        fields = ('profimg', 'rel_status', 'living', 'university', 'status')


class StatusForm(forms.ModelForm):

    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Leave a status!'}))

    class Meta:

        model = Status
        fields = ('content',)


"""class ProfilePicForm(forms.ModelForm):

    class Meta:

        model = UserProfile
        fields = ('profimg',)"""