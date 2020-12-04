from django import forms
from django.contrib.auth.models import User
from App1.models import UserInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')



#To create radiobutton introduce widget outside meta class
options = (('buyer', 'Buyer Account'), ('seller', 'Seller Account'))
class UserInfoForm(forms.ModelForm):
    BuyerOrSeller = forms.ChoiceField(choices = options, widget = forms.RadioSelect(), label = "Select the type of account:")

    class Meta():
        model = UserInfo
        fields = ('BuyerOrSeller',)
