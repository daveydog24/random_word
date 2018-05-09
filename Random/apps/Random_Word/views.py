# Have the following URL either display a simple HttpResponse or redirect to a different URL for the following apps
# blogs app
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
def index(request):
    if 'count' not in request.session:
        request.session["count"] = 1
    else:
        request.session["count"] += 1
    word = get_random_string(length=14)
    context = {
        "word": word
            }
    return render(request, "Random_Word/count.html", context)

def reset(request):
    if 'count' in request.session:
        del request.session['count']

    return redirect('/')