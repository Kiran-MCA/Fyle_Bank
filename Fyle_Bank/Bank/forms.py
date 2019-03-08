from django import forms

class IfscForm(forms.Form):
    Bank_ifsc = forms.CharField(label='Enter IFSC', max_length=100)



class BranchForm(forms.Form):
    Bank_Name = forms.CharField(label=' Bank Name', max_length=100)
    Bank_city = forms.CharField(label='Enter City', max_length=100)