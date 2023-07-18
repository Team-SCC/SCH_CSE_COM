from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os
from django.db.models import Q

from .models import Content

@login_required(login_url='common:login')
def cloud_main(request):
    '''클라우드 메인 화면 함수
    url: localhost:port/cloud/
    templates: cloud_main.html
    '''
    content_list = Content.objects.order_by('-create_date')
    page = request.GET.get('page', 1)
    content_list = content_list.filter(Q(author__student_id__icontains = request.user)).distinct()
    paginator = Paginator(content_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {'content_list':page_obj, 'page':page, 'kw':request.user}
    
    return render(request, 'cloud_main.html', context)

def content_delete(request, content_id):
    '''콘텐츠 삭제 함수
    url: localhost:port/cloud/delete/<int:content_id>/
    templates: None
    '''
    content = get_object_or_404(Content, pk=content_id)

    try:
        if content.file:
            os.remove(os.path.join(settings.MEDIA_ROOT, content.file.path))
    except:
        print(os.path.join(settings.MEDIA_ROOT, content.file.path))
        print('[cloud app, content_delete error]file does not exist.')
    
    content.delete()

    return redirect('cloud:cloud_main')

def content_create(request):
    '''콘텐츠 생성 함수
    url: localhost:port/cloud/create/
    templates: create.html
    '''

    if request.method == 'POST':
        for file in request.FILES.getlist('file'):
            form = Content()
            form.title = file
            form.create_date = timezone.now()
            form.author = request.user
            form.file = file
            form.save()

        return redirect('cloud:cloud_main')

    return render(request, 'create.html')

@login_required(login_url='common:login')
def file_download(request):
    '''파일 다운로드 함수
    url: localhost:port/cloud/download
    templates: None
    '''
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)
 
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '[cloud, views, file_download error] 파일이 존재하지 않습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")
