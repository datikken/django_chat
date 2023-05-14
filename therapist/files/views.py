from files.forms import DocumentFrom
from django.shortcuts import render


def index(request):
    form = DocumentFrom()
    return render(request, 'files/upload.html', { 'form': form })


def send_file(request):
    pass