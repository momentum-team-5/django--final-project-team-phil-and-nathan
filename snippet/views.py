from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Snippet
from .forms import SnippetForm, SearchForm
## import 404

#from django.contribu.auth import authenticate, login
#from .forms import PoemForm, CommentForm, ContactForm, SearchForm


# Create your views here.
def snippet_list(request):
    snippets = request.user.snippets.all()
    return render(request, "snippet/snippet_list.html", {"snippets": snippets})

def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, id=pk)
    return render(request, "snippet/snippet_detail.html", {"snippet": snippet})




@login_required
def add_snippet(request):
    if request.method == "GET":
        form = SnippetForm()

    else:
        form = SnippetForm(data=request.POST)

        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user # associate the new poem with the currently signed in user
            snippet.save()
 
            #success(request, "Your poem was created!")

            return redirect(to="snippet_list")
    return render(request, "snippet/add_snippet.html", {"form": form})


@login_required
def edit_snippet(request, pk):
    snippet = get_object_or_404(request.user.snippets.all(), pk=pk)

    if request.method == "GET":
        form = SnippetForm(instance=snippet)

    else:
        form = SnippetForm(data=request.POST, instance=snippet)

        if form.is_valid():
            form.save()  # We can save the form directly since the instance has already been created

           #success message

            return redirect(to="snippet_list")

        else:
            #error(request, "Your updates didn't work :(")
            pass

    return render(request, "snippet/edit_snippet.html", {"form": form})


@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(request.user.snippets.all(), pk=pk)
    snippet.delete()
    #success message

    return redirect(to="snippet_list")



def search(request):
    if request.method == "GET":
        form = SearchForm()

    else:
        form = SearchForm(data=request.POST)

        if form.is_valid():
            snippets = request.user.snippets.all()
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            language = form.cleaned_data['language']
            order_by = form.cleaned_data['order_by']

            if title:
                snippets = snippets.filter(title__contains=title)

            if body:
                snippets = snippets.filter(body__contains=body)
            
            if language:
                snippets = snippets.filter(language__exact=language)
            
            snippets = snippets.order_by(order_by)

            return render(request, "snippet/search_results.html", {"snippets": snippets})

    return render(request, "snippet/search.html", {"form": form})







def copy_snippet(request, pk):
    #snippet to be copied
    snippet = get_object_or_404(Snippet, pk = pk)
    snippet_copy = Snippet()
    snippet_copy.title = snippet.title
    snippet_copy.language = snippet.language
    snippet_copy.user = request.user

    #save the new snippet
    snippet_copy.save()

    #Add new snippet to copies of original
    snippet.copies.add(snippet_copy) 
        
