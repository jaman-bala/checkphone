from django.shortcuts import render, reverse
from .models import Base
from django.views.generic import FormView
from .forms import PhoneForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})

    else:
        form = PhoneForm()
    return render(request, 'index.html', {'form': form, 'index': index})
