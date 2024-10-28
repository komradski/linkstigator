from django import forms

class LinkForm(forms.Form):
    url = forms.URLField(        
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Article Link"}
        ),
    )
    # body = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"class": "form-control", "placeholder": "Leave a comment!"}
    #     )
    # )