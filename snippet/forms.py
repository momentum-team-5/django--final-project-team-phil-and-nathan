from django import forms
from .models import Snippet

LANGUAGE_CHOICES = (
        ("javascript", "javascript"),
        ("html", "html"),
        ("python", "python"),
        ("css", "css")
)

class SnippetForm(forms.ModelForm):

    
    language = forms.ChoiceField(choices = LANGUAGE_CHOICES, required=True, label="Select your language" )   

    class Meta:
        model = Snippet
        fields = [
            'title',
            'body',
            'language',
        ]


# Search should look for terms in the title, in other fields like a description  or tags, and in the language field. 
# If I search for "javascript auth," I should see any snippets I have about authentication using JavaScript.
#  See [search](https://docs.djangoproject.com/en/2.1/topics/db/search/) and
# search](https://docs.djangoproject.com/en/2.1/ref/contrib/postgres/search/) 
# in the Django documentation for some ideas.
class SearchForm(forms.Form):
    
    # This tuple provides selections for ordering the results
    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
        ("language", "language"),
    )

    # Form fields
    title = forms.CharField(max_length=255, required=False)
    body = forms.CharField(widget=forms.Textarea, required=False)
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=False)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)



 
