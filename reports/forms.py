from django import forms
 
class reportForm(forms.Form):
    activName = forms.CharField(
        required=True, 
        min_length=5,
        max_length=100, 
        label="",
        widget=forms.TextInput(attrs={"name": "activName", "class": "form-control shadow-none", "placeholder": "Например: TinkoffCTF 2024", "aria-label": "Например: TinkoffCTF 2024"}),
    )
    activDate = forms.DateField(
        required=True, 
        label="",
        widget=forms.DateInput(attrs={"name": "activDate", "type": "date", "class": "form-control shadow-none", "placeholder": "Например: 31.03.2024-2.04.2024", "aria-label": "Например: 31.03.2024-2.04.2024"}),
    )
    activLink = forms.CharField(
        required=False, 
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"name": "actvLink", "class": "form-control shadow-none", "placeholder": "Например: https://ctf.tinkoff.ru/profile", "aria-label": "Например: https://ctf.tinkoff.ru/profile"}),
    )
    activPlace = forms.IntegerField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={"name": "activPlace", "class": "form-control shadow-none", "placeholder": "Например: 386", "aria-label": "Например: 386"}),
    )
    activCertif = forms.FileField(
        required=False, 
        label="",
        widget=forms.FileInput(attrs={"name": "activCertif", "class": "form-control form-control-sm", "id": "formFileSm",}),
    )
    activOther = forms.CharField(
        required=False, 
        min_length=10, 
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"name": "activOther", "class": "form-control shadow-none", "placeholder": "Например: https://ctf.tinkoff.ru/scoreboard", "aria-label": "Например: https://ctf.tinkoff.ru/scoreboard"}),
    )
    activAddit = forms.CharField(
        required=False, 
        min_length=10, 
        max_length=200,
        label="",
        widget=forms.Textarea(attrs={"name": "activAddit", "class": "form-control shadow-none", "id": "exampleFormControlTextarea1", "rows": 3})
    )