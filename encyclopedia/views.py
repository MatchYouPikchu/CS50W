from django.http.response import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django import forms
from django.urls import reverse

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
            list=[]
            entries = util.list_entries()
            for item in entries:
                if (title.upper() in item.upper()):
                    list.append(item)
 
        return render(request, "encyclopedia/index.html", {
        "entries": list
    })

def create(request):

    if request.method == 'POST':
        form =(NewFileForm(request.POST))
        if form.is_valid():
            title = form.cleaned_data["title"]
            markdown = form.cleaned_data["markdown"]
            if (util.create_entry(title,markdown) == False):
                return HttpResponse("Sorry, filename exists, try new one")
            return HttpResponseRedirect(reverse("title", args = [title]))
    else:
        return render(request, "encyclopedia/create.html", {
            "form" : NewFileForm()
      } )

class NewFileForm(forms.Form):
    title = forms.CharField(label ="Title")
    markdown = forms.CharField(widget=forms.Textarea)
