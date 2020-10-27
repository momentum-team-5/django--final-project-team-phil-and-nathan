# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.mail import send_mail, mail_admins
# from django.contrib.messages import success, error
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .models import Poem, Comment
# from .forms import PoemForm, CommentForm, ContactForm, SearchForm



from django.contrib.auth.decorators import login_required
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


@login_required
def add_snippet(request):
    if request.method == "GET":
        form = SnippetForm()

    # else:
    #     form = SnippetForm(data=request.POST)

    #     if form.is_valid():
    #         snippet = form.save(commit=False)
    #         snippet.author = request.user # associate the new snippet with the currently signed in user
    #         snippet.save()

    #         success(request, "Your snippet was created!")

    #         return redirect(to="snippet_list")

    #     else:
    #         error(request, "Your snippet could not be created :(")

    return render(request, "snippets/add_snippet.html", {"form": form})
