from django.shortcuts import render
# Create your views here.
from . models import *

def index(request):
    return render(request, 'main/index.html', {'title': 'Main page'})
def tables(request):
    tables = User.objects.all()
    novels = Novel.objects.all()
    return render(request, 'main/table.html', {'tables': tables, 'novels': novels})
