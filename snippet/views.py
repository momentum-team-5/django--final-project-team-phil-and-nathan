from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Snippet
from django.contribu.auth import authenticate, login
#from .forms import PoemForm, CommentForm, ContactForm, SearchForm


# Create your views here.
def snippet_list(request):
    snippets = Snippet.objects.all()

    return render(request, "snippet/snippet_list.html", {"snippets": snippets})


# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return render(request, "snippet/snippet_list.html", {"snippets": Snippet.objects.filter(user=user)})
#     else:
#         # Return an 'invalid login' error message.
        
