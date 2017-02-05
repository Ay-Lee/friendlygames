from django import forms


class IFriendlyForm(forms.Form):
	CHOICES = (
		('U6', 'U6'),
		('U7', 'U7'),
    	('U8', 'U8'),
    	('U9', 'U9'),
    	('U10', 'U10'),
    	('U11', 'U11'),
    	('U12', 'U12'),
    	('U13', 'U13'),
        ('U14', 'U14(IP)'), 
    	('U15', 'U15'),
    	('U17', 'U17'),    	
    )
	leeftijd = forms.ChoiceField(choices=CHOICES, required=True, label='Leeftijd')
	datum = forms.CharField(label='datum', widget=forms.TextInput())
