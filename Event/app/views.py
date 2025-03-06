from django.shortcuts import render, redirect,reverse

from app import forms
from app.models import Event


# Create your views here.


def index(request):
    queryset = Event.objects.all()
    context = {"events": queryset}
    return render(request, "index.html",context)

def AskForEvent(request):
    if request.method == "POST":
        form_data = forms.EventForm(request.POST,files=request.FILES)
        if form_data.is_valid():
            event = form_data.save(commit=False)
            event.user = request.user
            event.poster = form_data.cleaned_data["poster"]
            event.save()
            return redirect(reverse("index"))
    context = {"form": forms.EventForm}
    return render(request, "AskForEvent.html",context=context)
