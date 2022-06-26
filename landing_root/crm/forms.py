from django import forms

class OrderForm(forms.Form):
    #create field djago form
    name = forms.CharField(max_length=200,required=False,widget=forms.TextInput(attrs={'class':'css_input'})) #optional field
    phone = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))