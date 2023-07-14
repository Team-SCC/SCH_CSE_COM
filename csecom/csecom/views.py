from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main.html')

def empty_page(request):
    return redirect('main')

@login_required(login_url='common:login')
def test_page(request):
    return render(request, 'test.html')
