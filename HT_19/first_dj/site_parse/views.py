from django.shortcuts import render
from .forms import MyModelForm, SaveModel


def do_parse(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        print(form["category"].value())
        to_save = SaveModel()
        to_save.save()

    form = MyModelForm
    context = {
        'form' : form
    }
    return render(request, 'site_parse/index.html', context)






