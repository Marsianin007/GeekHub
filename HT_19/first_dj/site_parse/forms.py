from .models import *
from django.forms import ModelForm

class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ["category"]