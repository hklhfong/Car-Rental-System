from django import forms
class NameForm(forms.Form):
    pickupCity = forms.CharField(label='Pickup City', max_length=100)
    dropoffCity = forms.CharField(label='Dropoff City', max_length=100)
    pickupDate = forms.DateField(label='Pickup date')
    dropoffDate = forms.DateField(label='Dropoff date')