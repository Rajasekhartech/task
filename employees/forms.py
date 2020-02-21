from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from .models import Profile
class UserForm(forms.ModelForm):
    choices = (("dept1", "dept1"), ("dept2", "dept2") )
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset= Group.objects.all())
    depatments_in_organization = forms.ChoiceField(help_text='Required. Select user department', choices=choices)
#    department = forms.ModelChoiceField(Profile.objects.all())
    class Meta:
        model = User
        fields = ['first_name', 'last_name' , 'email', 'username', 'password', 'depatments_in_organization' ]
        label = {'password' : 'Password' }

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None


        forms.ModelForm.__init__(self, *args, **kwargs)


    def save(self):
       password = self.cleaned_data.pop('password')
       role = self.cleaned_data.pop('role')
       u = super().save()
       u.groups.set([role])
       u.set_password(password)
       u.save()
       return u
