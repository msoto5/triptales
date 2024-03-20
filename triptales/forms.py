"""Forms for the triptales app."""
from django import forms
from triptales.models import Country, Location, VacationPost, UserProfile, Comment
from django.contrib.auth.models import User


class CountryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the name of the country.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Country
        fields = ('name', 'continent')
        help_texts = {
            'continent': 'Please select the continent of the country.'}



class LocationForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the name of the location.")
    country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('name'),
                                     help_text="Please choose the country where this location is.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    vibe = forms.RadioSelect()
    setting = forms.RadioSelect()
    travelPartners = forms.RadioSelect()
    climate = forms.RadioSelect()

    class Meta:
        model = Location
        exclude = ('views', 'posts')
        help_texts = {'vibe': 'What kind of vibe does this place give off?',
                      'setting': 'What type of setting is it?',
                      'travelPartners': 'What kind of partner is most suitable?',
                      'climate': 'What is the weather like here?', }


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
    location = forms.ModelChoiceField(queryset=Location.objects.all().order_by('name'), empty_label="Select Location", required=False)
    title = forms.CharField(help_text="Title")
    text = forms.CharField(help_text="Caption Here.")
    image = forms.ImageField(help_text="Please upload the image you wish to share")

    def __init__(self, *args, **kwargs):
        super(VacationPostForm, self).__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.all().order_by(
            'name')  # Set the queryset for the location field

    def clean_location(self):
        location = self.cleaned_data['location']
        if location and location in self.fields['location'].queryset:
            return location
        raise forms.ValidationError("Invalid location selection.")

    class Meta:
        model = VacationPost
        fields = ['title', 'text', 'image', 'location']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
