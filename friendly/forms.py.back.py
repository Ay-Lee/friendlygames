from django import forms


class IFriendlyForm(forms.Form):
	leeftijd = forms.CharField(label='Leeftijd', max_length=3)
	datum = forms.CharField(label='datum', max_length=10)

