from django.shortcuts import render
from .forms import MyModelForm
from .models import SaveModel


def do_parse(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        print(form["category"].value())
        model = SaveModel()
        model.save()



    form = MyModelForm()
    context = {
        'form' : form
    }
    return render(request, 'site_parse/index.html', context)








