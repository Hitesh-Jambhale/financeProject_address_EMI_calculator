from django import forms
from .models import PermanentAddress,CurrentAddress

class PermanentAddressForm(forms.ModelForm):
    class Meta :
        model = PermanentAddress
        fields = '__all__'

        # labels

        labels = {
            'flat_no': 'Flat No',
            'street_name': 'Street Name',
            'city': 'City',
            'pincode': 'Pincode',
            'area': 'Area',
            'landmark': 'Landmark',
            'district': 'District',
            'state': 'State',
            'country': 'Country'
        }



class CurrentAddressForm(forms.ModelForm):
    class Meta:
        model = CurrentAddress
        fields = '__all__'

        # labels

        labels = {
            'Cflat_no': 'Flat No',
            'Cstreet_name': 'Street Name',
            'Ccity': 'City',
            'Cpincode':'Pincode',
            'Carea': 'Area',
            'Clandmark':'Landmark',
            'Cdistrict':'District',
            'Cstate':'State',
            'Ccountry':'Country'
        }