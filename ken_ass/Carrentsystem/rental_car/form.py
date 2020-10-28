from django import forms


class PostForm(forms.Form):
    brand_name = forms.CharField(max_length=20, initial='')
    type = forms.CharField(max_length=2, initial='BMW')
    transmission = forms.DateField()
    price = forms.CharField(max_length=100, initial='', required=False)
    luggage_size = forms.CharField(max_length=20, initial='', required=False)
    seat_number = forms.CharField(max_length=20, initial='', required=False)
    release_year = forms.CharField(max_length=100, initial='', required=False)
