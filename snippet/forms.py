from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
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
    #This tuple will be used to implement different search types
    SEARCH_TYPES_CHOICES = (
        ("starts with", "starts with"),
        ("includes", "includes"),
        ("exact match", "exact match"),
    )

    # This tuple provides selections for ordering the results
    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
        ("language", "language"),
    )

    # Form fields
    title = forms.CharField(max_length=255, required=False)
    title_search_type = "includes"
    body = forms.CharField(widget=forms.Textarea, required=False)
    body_search_type = "includes"
    language = forms.CharField(widget=forms.CharField, required=False)
    language_search_type = "exact match"
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)

