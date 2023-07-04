from django.shortcuts import render, redirect

def main(request):
    return render(request, 'main.html')

def empty_page(request):
    return redirect('main')

def test_page(request):
    return render(request, 'test.html')

def temp_qanda(request):
    return render(request, 'qanda.html')
