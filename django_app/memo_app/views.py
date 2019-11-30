from django.shortcuts import render, redirect
from .forms import PostForm
from .models import *

def index(request):
    memos = Memo.objects.all()
    params = {
      'memos' : memos,
      'form': PostForm()
      }
    return render(request, 'index.html', params)

def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    return redirect(to='/')
