"""Forms for the triptales app."""
from django import forms
from triptales.models import Country, Location, VacationPost, UserProfile, Comment
from django.contrib.auth.models import User

class CountryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the name of the country.")
    continent = forms.CharField(help_text="Please enter the continent of this country.")

    class Meta:
        model = Country
        fields = ('name', 'continent')


class LocationForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the name of the location.")
    country = forms.ModelChoiceField(queryset=Country.objects)
    vibe = forms.RadioSelect()
    setting = forms.RadioSelect()
    travelPartner = forms.RadioSelect()
    climate = forms.RadioSelect()

    class Meta:
        model = Location
        exclude = ('views', 'posts')

class CommentForm(forms.ModelForm):
    text = forms.CharField(help_text="")

    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture', 'bio')


class VacationPostForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Select Country")
    location = forms.ModelChoiceField(queryset=Location.objects.none(), required=False)  # Initially empty or not required
    text = forms.CharField(help_text="Caption Here.")
    image = forms.ImageField(help_text="Please upload the image you wish to share")
    
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


