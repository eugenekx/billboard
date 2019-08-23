from django import forms
import urllib

class EventForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Название'}), required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control mb-3 choosedate', 'placeholder': 'Дата'}), required=False)
    price_from = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'от'}), required=False)
    price_to = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'до'}), required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'напр.: инди'}), required=False)

class ArtistForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Имя/название'}), required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'напр.: инди'}), required=False)


class OrgForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Имя/название'}), required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'напр.: инди'}), required=False)

class PlaceForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Имя/название'}), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Адрес'}), required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'напр.: клуб, лекторий'}), required=False)