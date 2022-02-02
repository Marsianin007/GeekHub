from django.shortcuts import render
from .forms import MyModelForm
from .models import AskModel


def do_parse(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        print(form["category"].value())
        if form["category"].value() == "askstories":
            model = AskModel()
            model.save()

    form = MyModelForm()
    context = {
        'form' : form
    }
    return render(request, 'site_parse/index.html', context)








