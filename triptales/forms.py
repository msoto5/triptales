"""Forms for the triptales app."""
from django import forms
from triptales.models import Country, Location, VacationPost

class VacationPostForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Country")
    location = forms.ModelChoiceField(queryset=Location.objects.none(), required=False)  # Initially empty or not required
    
    def __init__(self, *args, **kwargs):
        super(VacationPostForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            instance = kwargs['instance']
            if instance and instance.country:
                self.fields['location'].queryset = Location.objects.filter(country=instance.country)
            else:
                self.fields['location'].queryset = Location.objects.none()
        elif 'initial' in kwargs and 'country' in kwargs['initial']:
            country_id = kwargs['initial']['country']
            self.fields['location'].queryset = Location.objects.filter(country_id=country_id)
        else:
            self.fields['location'].queryset = Location.objects.none()

    class Meta:
        model = VacationPost
        fields = ['text', 'image', 'country', 'location']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }


