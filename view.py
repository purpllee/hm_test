from django.http import Httpresponse
from django.shortcuts import redirect
def index(request):
    return Httpresponce('index')

def login(request):
    return redirect('/index')
