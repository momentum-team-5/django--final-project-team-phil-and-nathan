from django.shortcuts import render, get_object_or_404

from .models import Snippet
from .forms import SnippetForm

# Create your views here.

def snippets_list(request):
    snippets = Snippet.objects.all()

    return render(request, "snippets/snippets_list.html", {"snippets": snippets})

def snippets_detail(request, pk):
    snippet = get_object_or_404(Snippet, id=pk)

    return render(request, "snippets/snippets_detail.html", {"snippet": snippet})





#     from .models import Note
# from .forms import NoteForm


# # Create your views here.
# def notes_list(request):
#     notes = Note.objects.all()

#     return render(request, "notes/notes_list.html", {"notes": notes})