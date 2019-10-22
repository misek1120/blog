from django import forms
from .models import Record, User
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
#from django.contrib.auth.models import User

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields =["title","image", "author", "genre","summary",
                "impressions", "learn", "story", "user",
                "difference", "importance", "agree", "opposition",
                "unkown", "example", "inspiration"]
        widgets = {
            'user': forms.HiddenInput,
            #'image': forms.ImageField(attrs={'height':100, 'width':100}),
            'summary': forms.Textarea(attrs={'cols':100,'rows':1}),
            'impressions': forms.Textarea(attrs={'cols':100,'rows':1}),
            'learn': forms.Textarea(attrs={'cols':100,'rows':1}),
            'story': forms.Textarea(attrs={'cols':100,'rows':1}),
            'difference': forms.Textarea(attrs={'cols':100,'rows':1}),
            'importance': forms.Textarea(attrs={'cols':100,'rows':1}),
            'agree': forms.Textarea(attrs={'cols':100,'rows':1}),
            'opposition': forms.Textarea(attrs={'cols':100,'rows':1}),
            'unkown': forms.Textarea(attrs={'cols':100,'rows':1}),
            'example': forms.Textarea(attrs={'cols':100,'rows':1}),
            'inspiration': forms.Textarea(attrs={'cols':100,'rows':1}),
        }
    """def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['height']=100
        self.fields['image'].widget.attrs['widget']=100
        """

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username", "password1", "password2",)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "full_name", "email",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'email'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for field in self.fields.values():
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザーネーム'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
#class SearcRecordForm(forms.Form):
#    target = forms.CharField(
#            initial='',
#            label='検索',
#            required = False,
#    )
