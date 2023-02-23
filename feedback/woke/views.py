from django.shortcuts import render
from django.http import HttpResponse
from .models import db
from .forms import db_form
# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, "index.html",{'form': db_form})
    else:
        form=db_form(request.POST,request.FILES or None)
        if form.is_valid:
            form.save()
            return render(request, "index.html",{'form': db_form})
        else:
            return HttpResponse("form not valid")
def about(request):
    return render(request, "about.html")

