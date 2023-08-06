from django.shortcuts import render

def info_main(request):
    return render(request, 'info_main.html')
