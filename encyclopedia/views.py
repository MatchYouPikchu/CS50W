from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if (util.get_entry(title)):
        return render(request,"encyclopedia/title.html" ,{
            "title" : title,
            "entry" : util.get_entry(title)
            })
    else:
        return HttpResponse("Requested page was not found")
     

def search(request):
    if request.method =='GET': 
        title = request.GET['q']
        if (util.get_entry(title)):
            return render(request,"encyclopedia/title.html" ,{
            "title" : title,
            "entry" : util.get_entry(title)
            })
        else:
            return HttpResponse("Requested page was not found")
# I can use the in method
