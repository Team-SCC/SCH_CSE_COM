from django.shortcuts import render, redirect

def main(request):
    return render(request, 'main.html')

def empty_page(request):
    return redirect('main')
