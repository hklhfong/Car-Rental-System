from django import forms
class NameForm(forms.Form):
    pick_up_city = forms.CharField(label='Pickup City', max_length=100)
    drop_off_city = forms.CharField(label='Dropoff City', max_length=100)
    pick_up_date = forms.DateField(label='Pickup date')
    drop_off_date = forms.DateField(label='Dropoff date')