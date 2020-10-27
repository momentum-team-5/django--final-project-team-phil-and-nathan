from django.shortcuts import render, get_object_or_404
from .models import Snippet

# Create your views here.
def copy_snippet(request, pk):
    # snippet to be copied
    snippet = get_object_or_404(Snippet, id=pk)

    # 
    snippet_copy = Snippet()
    snippet_copy.title = snippet.title
    snippet_copy.language = snippet.language
    snippet_copy.user = request.user

    # save the new snippet
    snippet_copy.save()

    # Add new snippet to copies of original
    snippet.copies.add(snippet_copy)
