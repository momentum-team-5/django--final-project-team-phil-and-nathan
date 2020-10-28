from django.shortcuts import render, redirect
from snippet import models
from django.contrib.auth import authenticate, login

#sendmail("message subject, message body", ["fackhackemail.net"], fail_silenly=True)

# def user_view(request, pk):
#     snippets = models.Snippet.objects.filter(author=request.user)
#     if request.user.id == pk:
#         return render(request, "user_snippet_list.html", {"snippets": snippets})
#     else: 
#         return render(request, "anon_snippet_list.html", {"snippets": snippets})




# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect(to="user_view", pk = user.id )
#     else:
#         pass

