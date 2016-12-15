from django.shortcuts import render
from .forms import TestFieldForm
# Create your views here.
def test(request):
    context = {}
    context['form'] = TestFieldForm()
    return render(request,'base.html',context)
